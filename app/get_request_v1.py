from flask_restful import Resource, Api # import the Resource class from the flask_restful module
from flask import Flask, request, jsonify # import the request object from the flask module
from app.limiter import limiter # Import the limiter instance from the limiter 
from marshmallow import ValidationError # import the ValidationError class from the marshmallow module
from app.schemas import UserSchema # import the UserSchema class from the schemas module
from flask_oauthlib.provider import OAuth2Provider # import the OAuth2Provider class from the flask_oauthlib.provider module
from app.auth import require_api_key # import the require_api_key function
#from functools import wraps 


print ('starting flask app')

class getRequestV1(Resource): # create a class named getRequestV1 that inherits from the Resource class
    
    oauth = OAuth2Provider()

    #decorators = [limiter.limit("5 per minute"), require_api_key]  # Correct usage of limiter instance
    decorators = [limiter.limit("5 per minute", key_func=lambda: request.headers.get('X-Api-Key')), require_api_key]
    #decorators = [limiter.limit("5 per minute")]
    print("still working")
    
    
    def get(self): # create a get method
        print("Get method works")
        return {"message" : 'Version1 hello world'} # return the string 'Version1 hello world'
   
   
   
    def post(self): # create a post method
        print("Post method works")
        user_schema = UserSchema() # create an instance of the UserSchema class
        
        try: # try block
            json_data = request.get_json() 
            print("here is the statement", type(json_data))
            data = user_schema.load(json_data) # get the JSON data from the request
            
            data_without_sets = {} # create an empty dictionary

            for key, value in data.items(): # iterate over the key-value pairs in the data dictionary
                if (isinstance(value, set)): # check if the value is a set
                    data_without_sets[key] = list(value) # convert the set to a list and add it to the data_without_sets dictionary
                else:
                    data_without_sets[key] = value # add the key-value pair to the data_without_sets dictionary
            
            return {"message": f'Hello {data["name"]}! this is version 1, your email is {data_without_sets["email"]}'} # return a formatted string with the name from the JSON data
        
        except ValidationError as err:

            return {"message": 'N/A please input..'}, 400



    


#command to make post request curl -X POST  http://127.0.0.1:5000/v1/hello -H "x-api-key: 28/2/24" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "rfernandez@gmail.com"}' 
#command to make get request curl -X GET http://127.0.0.1:5000/v1/hello -H "x-api-key: 28/2/24"

#so if the instance is a set (ifinstance(value, set), then it becomes a dictionary set by key: list(value), and it the instance is not a set it keeps it the same (else value for key), and value in data. The data.items() is iterated to find tuples that have key-value pairs from data
#fix running, and test the code
#throttling should work globally and for user as well, each user should have a limit of 5 requests per minute, should be able to set between per user or globally, if and else statement