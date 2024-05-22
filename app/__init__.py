from flask import Flask # import Flask class from the flask module
from flask_restful import Api #import Api class from the flask_restful module
from .limiter import limiter  # Import the limiter instance
from app.oauth import configure_oauth #Import configure_oauth class from app.oauth module

app = Flask(__name__) # create an instance of the Flask class with the name of the running application as the argument

def create_app(): # create a function named create_app

    api = Api(app) # create an instance of the Api class with the app instance as the argument
    limiter.init_app(app) # Initialize the limiter with the app
    configure_oauth(app)

    from .resources.get_request_v1 import getRequestV1 # import the getRequestV1 class from the resources module
    from .resources.get_request_v2 import getRequestV2 # import the getRequestV2 class from the resources module

    api.add_resource(getRequestV1, '/v1/hello') # add the getRequestV1 resource to the api with the route '/v1/hello'
    api.add_resource(getRequestV2, '/v2/hello') # add the getRequestV2 resource to the api with the route '/v2/hello'

    @app.route('/') # create a route for the root URL
    def index(): # create a function named index
        return 'Welcome' # return the string 'Welcome'

    from . import auth # import the auth module
    return app # return the app instance
