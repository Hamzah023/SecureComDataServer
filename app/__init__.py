from flask import Flask, request, jsonify # import Flask class from the flask module
from flask_restful import Api #import Api class from the flask_restful module
from flask_limiter import Limiter # Import the limiter instance
from app.oauth import configure_oauth #Import configure_oauth class from app.oauth module
from .auth import require_api_key
from .get_request_v1 import getRequestV1 # import the getRequestV1 class from the resources module
from .get_request_v2 import getRequestV2 # import the getRequestV2 class from the resources module
from flask_limiter.errors import RateLimitExceeded
from .limiter import getApiKey
from flask_limiter.util import get_remote_address
from .utils import init_apdp, limiter_instance

def create_app(): # create a function named create_app
    app = Flask(__name__) # create an instance of the Flask class with the name of the running application as the argument  
    api = Api(app) # create an instance of the Api class with the app instance as the argument
   
    
    '''@app.errorhandler(RateLimitExceeded)
    def ratelimit_handler(e):
        return jsonify({'message': 'You have exceeded the request rate limit'}), 429 
    '''

    '''limiter = Limiter(
        app=app, 
        key_func=get_remote_address, 
        default_limits=["1000 per minute"]
    )
    '''
    
    init_apdp(app) # initialize the limiter with your Flask app using the init_app method and configure the error handler.
    
    print("resource v1 is being added to api")
    api.add_resource(getRequestV1, '/v1/hello') # add the getRequestV1 resource to the API with the route '/v1/hello'   
    print("resource v2 is being added to api")
    api.add_resource(getRequestV2, '/v2/hello') # add the getRequestV2 resource to the API with the route '/v2/hello'   

    print("resource v3 is being added to api")

    @app.route('/') # create a route for the root URL
    def index(): # create a function named index
        return jsonify({"message": 'Welcome'}) # return the string 'Welcome'

    @app.route('/v1/API', methods=['GET'])
    @require_api_key
    def protectedRoute():
        return jsonify({"message": "API KEY is valid (v1)"})

    @app.route('/v2/API', methods=['GET'])
    @require_api_key
    def v2ProtectedRoute():
        return jsonify({"message": "API KEY valid (V2)"})

    @app.route('/unprotected', methods = ['GET'])
    def unprotectedRoute():
        return jsonify({"message": "This route is unprotected"})

    return app # return the app instance

    #-COMMANDS-
    # to make a post request to the protected route, use the following command: curl -X GET http://127.0.0.1:5000/v1/API -H "x-api-key: 28/2/24"
    # to make a post request to the unprotected route, use the following command: curl -X GET http://127.0.0.1:5000/   
