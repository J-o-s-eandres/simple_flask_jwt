from flask import Blueprint, request,jsonify
from function_jwt import write_token,validate_token
routes_auth = Blueprint("routes_auth", __name__)

@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data['username'] == "Joseandres Montesino":
        return write_token(data=request.get_json())
    else:
        response =jsonify({"message":"User not fount"})
        response.status_code=404
        return response
    
    
@routes_auth.route("/verify/token")
def verify():
    token=(request.headers["Authorization"].split(" ") [1])
    return validate_token(token, output=True)
    