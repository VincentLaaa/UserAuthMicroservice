# UserAuthMicroservice

# Requesting Data:
To request data from the User Authentication Microservice, follow these steps:

1) Download the Microservice:
Download the user_authentication_microservice.py file from the GitHub repository.

3) Import the Microservice:
Import the UserAuthenticationMicroservice class into your Python program.

5) Initialize the Microservice:
Create an instance of the UserAuthenticationMicroservice class.


# Receiving Data: 
Once you have downloaded and imported the microservice, you can use it locally in your Python program.

```Example Program:

from user_authentication_microservice import UserAuthenticationMicroservice

def sign_up(auth_microservice):
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")
    if auth_microservice.sign_up(username, password):
        print("User registered successfully")
    else:
        print("Username already exists or password does not meet requirements")

def sign_in(auth_microservice):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if auth_microservice.sign_in(username, password):
        print("Login successful")
    else:
        print("Invalid username or password")

def main():
    # Initialize the microservice
    auth_microservice = UserAuthenticationMicroservice()

    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sign_up(auth_microservice)
        elif choice == "2":
            sign_in(auth_microservice)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

# UML Sequence Diagram (Look through edit view, formatting is weird if not)

Client                  User Authentication Microservice
  |                                   |
  |      sign_up(username, password) |
  |---------------------------------->|
  |                                   |
  |          validate_password()     |
  |---------------------------------->|
  |                                   |
  |         save_user_credentials()  |
  |---------------------------------->|
  |                                   |
  |      [Registration Success]      |
  |<----------------------------------|
  |                                   |
  |                                   |
  |       sign_in(username, password)|
  |---------------------------------->|
  |                                   |
  |      [Login Success/Failure]     |
  |<----------------------------------|
  |
