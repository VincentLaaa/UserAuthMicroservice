# UserAuthMicroservice

This User Authentication Microservice handles user authentication, signing in and signing up. The service users ZeroMQ for the communication.

# Requesting Data:
To request data from the User Authentication Microservice, send a JSON object that contains the action sign_in or sign_up, the username and then the password to the ZeroMQ Server.

**Example Request:**

Signing in
```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = {
    "action": "sign_in",
    "username": "exampleUser",
    "password": "examplePassword"
}
socket.send_json(request)
response = socket.recv_json()
print(response)
```

Singing Up
```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = {
    "action": "sign_up",
    "username": "exampleUser",
    "password": "ExamplePassword1!"
}
socket.send_json(request)
response = socket.recv_json()
print(response)
```

# Receiving Data: 
The microservice will respond with a JSON object indicating the success of the request and a message.

Sign in Receiving Data
```
{
    "success": True,
    "message": "Successfully signed in!"
}

```
Sign up Receiving Data
```
{
    "success": True,
    "message": "Successfully signed up!"
}

```
**Running the Microservice**
To run the microservice use this command:
```python user_auth_service.py```

# UML Sequence Diagram (Look through edit view, formatting is weird if not)

Client                  User Authentication Microservice
       |                                             |
       |           (1) Send Request (JSON)           |
       |-------------------------------------------->|
       |                                             |
       |                                             |
       |        (2) Process Request (sign_in or      |
       |                sign_up)                     |
       |                                             |
       |                                             |
       |           (3) Send Response (JSON)          |
       |<--------------------------------------------|
       |                                             |
       |                                             |
