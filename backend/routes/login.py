from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash

from datetime import timezone, datetime, timedelta

from database.database import get_user_info_for_login

import datetime
import jwt

login_route_blueprint = Blueprint("login_route", __name__, url_prefix=("/api"))

@login_route_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    # autofill details for errors
    autofill_details = {
        "username": username,
        "password": password
    }

    # get user if they exist
    user = get_user_info_for_login(username)

    # check that a user exists 
    if not user: # user doesnt exist
        return jsonify({
            "error": True,
            "message": "Username does not exist.",
            "autofill": autofill_details
        }), 400
    
    # user does exist so check password with stored hashed one
    passwords_match = check_password_hash(user["password"], password)

    if not passwords_match: # incorrect password
        return jsonify({
            "error": True,
            "message": "Incorrect password.",
            "autofill": autofill_details
        }), 400
    
    # user entered correct details so sign jwt and return to front end and log user in
    
    # create expiration time variable so code is cleaner
    expiration = datetime.now(timezone.utc) + timedelta(days=3)
    
    token = jwt.encode({
        "user_id": user["id"],
        "exp": expiration
    }, current_app.config["JWT_SECRET_KEY"])

    # return jwt
    return jsonify({
        "error": False,
        "Message": "User logged in.",
        "token": token,
    }), 200

