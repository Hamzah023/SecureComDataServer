from flask import Flask, request, jsonify # import Flask class from the flask module
from flask_restful import Api #import Api class from the flask_restful module
from .limiter import limiter  # Import the limiter instance
from app.oauth import configure_oauth #Import configure_oauth class from app.oauth module
from .auth import require_api_key
from .get_request_v1 import getRequestV1 # import the getRequestV1 class from the resources module
from .get_request_v2 import getRequestV2 # import the getRequestV2 class from the resources module




def create_app(): # create a function named create_app
    app = Flask(__name__) # create an instance of the Flask class with the name of the running application as the argument  
    api = Api(app) # create an instance of the Api class with the app instance as the argument
    limiter.init_app(app) # Initialize the limiter with the app
    configure_oauth(app)

    print("resource v1 is being added to api")
    api.add_resource(getRequestV1, '/v1/hello') # add the getRequestV1 resource to the API with the route '/v1/hello'   
    print("resource v2 is being added to api")
    api.add_resource(getRequestV2, '/v2/hello') # add the getRequestV2 resource to the API with the route '/v2/hello'   

    print("resource v3 is being added to api")

    @app.route('/') # create a route for the root URL
    def index(): # create a function named index
        return jsonify({"message": 'Welcome'}) # return the string 'Welcome'

    @app.route('/v1/API', methods=['POST'])
    @require_api_key
    def protectedRoute():
        return jsonify({"message": "API KEY is valid (v1)"})

    @app.route('/v2/API', methods=['POST'])
    @require_api_key
    def v2ProtectedRoute():
        return jsonify({"message": "API KEY valid (V2)"})

    @app.route('/unprotected', methods = ['POST'])
    def unprotectedRoute():
        return jsonify({"message": "This route is unprotected"})

    return app # return the app instance

