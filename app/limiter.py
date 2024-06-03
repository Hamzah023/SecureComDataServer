# app/limiter.py
from flask import Flask
from flask_limiter import Limiter, RateLimitExceeded
from flask import jsonify, request

#this is for if you want to limit the number of requests per minute via api-key, a sort of global limiting
def getApiKey():
    print("getApiKey is being called")
    apiKey = request.headers.get('x-api-key')
    print(apiKey)
    return request.headers.get('x-api-key')

limiter = Limiter(key_func=getApiKey, default_limits=["5 per 1 minuute"])


