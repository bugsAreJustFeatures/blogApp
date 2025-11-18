from flask import Blueprint, current_app, request, jsonify

from werkzeug.security import generate_password_hash

from database.database import edit_password

from utils.decode_jwt import decode_jwt

edit_password_blueprint = Blueprint("edit_password", __name__, url_prefix="/api")

@edit_password_blueprint.route("/edit-password", methods=["POST"])
def edit_password_route():
    data = request.get_json()

    # decode jwt and get user_id
    decoded_jwt = decode_jwt(current_app, request)
    user_id = decoded_jwt["user_id"]

    new_password = data["newPassword"]
    new_confirm_password = data["newConfirmPassword"]

    # check they both match
    if not new_password == new_confirm_password: 
        return jsonify({
            "error": True,
            "message": "Passwords do not match."
        }), 400
    
    # check the password meets the same criteria as the password when making an account
    if len(new_password) < 8: # check password is too short
        return jsonify({
            "error": True,
            "message": "Password is too short. It needs to be 8+ characters long.",
        }), 400
    elif not new_password.isascii():
        return jsonify({
            "error": True,
            "message": "Password can only contain ASCII characters.",
        }), 400 
    
    # generate hashed password to store in db
    hashed_password = generate_password_hash(new_password)

    # edit password in db
    edit_password(user_id, hashed_password)

    return jsonify({
        "error": False,
        "message": "Password changed successfully."
    }), 200