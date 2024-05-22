from flask_restful import Resource # import the Resource class from the flask_restful module
from flask import request # import the request object from the flask module
from app.limiter import limiter # Import the limiter instance from the limiter 
from marshmallow import ValidationError # import the ValidationError class from the marshmallow module
from app.schemas import UserSchema # import the UserSchema class from the schemas module
from flask_oauthlib.provider import OAuth2Provider # import the OAuth2Provider class from the flask_oauthlib.provider module
from app.auth import require_api_key # import the require_api_key function

class getRequestV1(Resource): # create a class named getRequestV1 that inherits from the Resource class
    
    oauth = OAuth2Provider()

    decorators = [limiter.limit("5 per minute"), require_api_key]  # Correct usage of limiter instance

    def get(self): # create a get method
        return 'Version1 hello world' # return the string 'Version1 hello world'

    def post(self): # create a post method
        user_schema = UserSchema() # create an instance of the UserSchema class
        
        try: # try block

            data = user_schema.load(request.get_json()) # get the JSON data from the request
            data_without_sets = {key: list(value) if isinstance(value, set) else value for key, value in data.items()} # create a dictionary comprehension to convert sets to lists
            
            return f'Hello {data["name"]}! this is version 1, your email is {data_without_sets["email"]}' # return a formatted string with the name from the JSON data
        
        except ValidationError as err:
            return {'message': 'N/A please input wtf dawg'}, 400


#command to make post request curl -X POST http://127.0.0.1:5000/v1/hello -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 30, "interests": ["reading", "traveling"], "unique_ids": [1, 2, 3]}'
#curl -X POST http://127.0.0.1:5000/v1/hello -H "Content-Type: application/json" -d '{"name": "Rachel", "email": "rfernandez@gmail.com"}'
#command to make get request curl -X GET http://
#so if the instance is a set (ifinstance(value, set), then it becomes a dictionary set by key: list(value), and it the instance is not a set it keeps it the same (else value for key), and value in data. The data.items() is iterated to find tuples that have key-value pairs from data