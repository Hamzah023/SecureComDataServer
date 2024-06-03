from flask import Flask, request, jsonify 
from functools import wraps 
import schedule
import time
import random
import threading

def scheduler():
    while True:
        schedule.run_pending() #run the pending tasks like update_api_key
        time.sleep(1) #sleep for 1 second for break 
    
schedule_thread = threading.Thread(target=scheduler)
schedule_thread.daemon = True
schedule_thread.start()

def make_api_key(count, min_value=100000, max_value=999999):
        
        return [random.randint(min_value, max_value) for _ in range(count)]
    
API_KEY = make_api_key(1)
    
print(f"The api key is {API_KEY}")


def require_api_key(f):
    @wraps(f) # This is a decorator that wraps the decorated function
    def decoratedFunction(*args, **kwargs):
        recieved_api_key = request.headers.get('X-Api-Key')
        if recieved_api_key == str(API_KEY):
            return f(*args, **kwargs)
        else:
            print(f"recieved API key: {recieved_api_key}")
            print(f"Expected API key: {API_KEY}")
            return {'message': 'Invalid API KEY'}, 401
        
    return decoratedFunction

def update_api_key():
    global API_KEY
    API_KEY = make_api_key(1)
    print(f"The updated api key is {API_KEY}")
    return API_KEY

schedule.every(5).minutes.do(update_api_key) #the 1 argument is the count of the api key which means 1 api key will be generated every 2 minutes



'''
api key is randomly generated
client sends get request to the server asking for the api key
server sends the api key to the client
client sends a post request to the server with the api key
'''