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



