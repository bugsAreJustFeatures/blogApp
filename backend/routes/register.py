from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from database.database import does_username_exist, register_user

register_route_blueprint = Blueprint("register_route", __name__, url_prefix="/api")

@register_route_blueprint.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    first_name = data["firstName"]
    last_name = data["lastName"]
    username = data["username"]
    password = data["password"]
    confirm_password = data["confirmPassword"]

    # make autofill object for form on frontend for errors
    autofill_details = {
        "firstName": first_name,
        "lastName": last_name,
        "username": username,
        "password": password,
        "confirmPassword": confirm_password
    }

    ## check username 

    # check username doesnt already exist
    username_taken = does_username_exist(username)

    if username_taken: # username already taken so return error message
        return jsonify({
            "error": True,
            "message": "Username already exists.",
            "autofill": autofill_details
        }), 409
    
    if len(username) < 3 or len(username) > 12: # check length of username
        return jsonify({
            "error": True,
            "message": "Username must be between 3 and 12 character long.",
            "autofill": autofill_details
        }), 400
    elif not username.isalnum(): # check username is alphanumerical
        return jsonify({
            "error": True,
            "message": "Username can only be alphumerical.",
            "autofill": autofill_details
        }), 400
    
    ## check passwords
    
    # compare passwords and check they are the same
    if not password == confirm_password:
        return jsonify({
            "error": True,
            "message": "Passwords do not match.",
            "autofill": autofill_details
        }), 400
    elif len(password) < 8: # check password is not short
        return jsonify({
            "error": True,
            "message": "Password is too short. It needs to be 8+ characters long.",
            "autofill": autofill_details
        }), 400
    elif not password.isascii():
        return jsonify({
            "error": True,
            "message": "Password can only contain ASCII characters.",
            "autofill": autofill_details
        }), 400
    
    
    # hash password
    hashed_password = generate_password_hash(password)

    # store user details in db
    register_user(first_name, last_name, username, hashed_password)

    # return success message
    return jsonify({
        "error": False,
        "message": "Registered Successfully."
    }), 201
