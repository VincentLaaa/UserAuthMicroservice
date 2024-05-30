import os
import hashlib
import re
import zmq
import json

class UserAuthenticationMicroservice:
    def __init__(self, credentials_file="user_credentials.txt"):
        self.credentials_file = credentials_file

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_user_credentials(self):
        user_credentials = {}
        if os.path.exists(self.credentials_file):
            with open(self.credentials_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(":")
                    user_credentials[username] = password
        return user_credentials

    def save_user_credentials(self, user_credentials):
        with open(self.credentials_file, "w") as file:
            for username, password in user_credentials.items():
                file.write(f"{username}:{password}\n")

    def validate_password(self, password, username):
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if not re.search(r"\d", password):
            return False, "Password must include at least one number (0-9)."
        if not re.search(r"[A-Z]", password):
            return False, "Password must include at least one uppercase letter (A-Z)."
        if not re.search(r"[!@#$%^&*()_+=\-[\]{};:'\"|,.<>/?]", password):
            return False, "Password must include at least one special character."
        common_words = ["password", "123456", "qwerty", "letmein"]
        if any(word.lower() in password.lower() for word in common_words):
            return False, "Password should avoid common words or phrases."
        if username.lower() in password.lower() or any(part.lower() in password.lower() for part in username.split()):
            return False, "Password should not contain your username or any part of your name."
        return True, "Password meets all requirements."

    def sign_in(self, username, password):
        user_credentials = self.load_user_credentials()
        hashed_password = self.hash_password(password)
        if username in user_credentials and user_credentials[username] == hashed_password:
            return {"success": True, "message": "Successfully signed in!"}
        return {"success": False, "message": "Invalid username or password."}

    def sign_up(self, username, password):
        user_credentials = self.load_user_credentials()
        if username in user_credentials:
            return {"success": False, "message": "Username already exists. Please choose a different username."}
        is_valid, message = self.validate_password(password, username)
        if not is_valid:
            return {"success": False, "message": message}
        hashed_password = self.hash_password(password)
        user_credentials[username] = hashed_password
        self.save_user_credentials(user_credentials)
        return {"success": True, "message": "Successfully signed up!"}


def main():
    auth_service = UserAuthenticationMicroservice()
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_json()
        action = message.get("action")
        username = message.get("username")
        password = message.get("password")

        if action == "sign_in":
            response = auth_service.sign_in(username, password)
        elif action == "sign_up":
            response = auth_service.sign_up(username, password)
        else:
            response = {"success": False, "message": "Unknown action."}

        socket.send_json(response)

if __name__ == "__main__":
    main()
