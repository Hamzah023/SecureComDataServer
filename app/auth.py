from flask import Flask, request, jsonify 
from functools import wraps 



API_KEY = "28/2/24"

def require_api_key(f):
    @wraps(f) # This is a decorator that wraps the decorated function
    def decoratedFunction(*args, **kwargs):
        if request.headers.get('X-Api-Key') == API_KEY:
            return f(*args, **kwargs)
        else:
            return {'message': 'Invalid API KEY'}, 401
        
    return decoratedFunction


'''
api key is randomly generated
client sends get request to the server asking for the api key
server sends the api key to the client
client sends a post request to the server with the api key
'''