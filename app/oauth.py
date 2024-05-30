from flask_oauthlib.provider import OAuth2Provider # import the OAuth2Provider class from the flask_oauthlib.provider module

oauth = OAuth2Provider() # create an instance of the OAuth2Provider class

def configure_oauth(app): # create a function named configure_oauth with the app instance as the argument
    oauth.init_app(app) # initialize the oauth instance with the app instance
