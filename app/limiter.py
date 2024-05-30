# app/limiter.py
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address) # Create an instance of the Limiter class with the get_remote_address function as the key_func argument
#get_remote_address is a function that returns the IP address of the client making the request
