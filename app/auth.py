from flask import Flask, request, jsonify
from functools import wraps 
from . import app



API_KEY = "28/2/24"

def require_api_key(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if request.headers.get('x-api-key') == API_KEY:
            return f(*args, **kwargs)
        else:
            return jsonify ({"message": "Invalid API KEY"}), 401
    return decoratedFunction

@app.route('/v1/API', methods=['GET', 'POST'])
@require_api_key
def protectedRoute():
    return jsonify({"message": "API KEY is valid (v1)"})

@app.route('/v2/API', methods=['GET', 'POST'])
@require_api_key
def v2ProtectedRoute():
    return jsonify({"message": "API KEY valid (V2)"})

@app.route('/unprotected', methods = ['GET', 'POST'])
def unprotectedRoute():
    return jsonify({"message": "This route is unprotected"})

for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == '__main__':
    app.run(debug=True)
