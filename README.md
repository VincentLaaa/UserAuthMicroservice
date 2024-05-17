# UserAuthMicroservice

# Requesting Data:
To request data from this microservice do the following:

1) Send a HTTP Post request to the appropriate endpoint (/sign_up for registration or /sign_in for login).
2) Include the username and password as JSON data in the request body.

# Example call for signing up:
import requests

url = "http://your_microservice_url/sign_up"
data = {"username": "example_user", "password": "example_password"}
response = requests.post(url, json=data)
print(response.json())

# Example for signing in:
import requests

url = "http://your_microservice_url/sign_in"
data = {"username": "example_user", "password": "example_password"}
response = requests.post(url, json=data)
print(response.json())

# Receiving Data: 
To programmatically receive data from the User Authentication Microservice, handle the HTTP response returned by the microservice.

The response will contain a JSON object with a message indicating the outcome of the request.
Example response format:

{"message": "Login successful"}

# UML Sequence Diagram

Client                    User Authentication Microservice
   |                                      |
   |          sign_up(username, password) |
   |------------------------------------->|
   |                                      |
   |         [Username does not exist]    |
   |<-------------------------------------|
   |                                      |
   |       validate_password(password)    |
   |------------------------------------->|
   |                                      |
   |          save_user_credentials()     |
   |------------------------------------->|
   |                                      |
   |          [Registration Success]      |
   |<-------------------------------------|
   |                                      |
   |                                      |
   |           sign_in(username, password)|
   |------------------------------------->|
   |                                      |
   |            [Login Success]           |
   |<-------------------------------------|
   |                                      |
