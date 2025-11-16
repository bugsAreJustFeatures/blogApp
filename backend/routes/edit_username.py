from flask import Blueprint, current_app, request, jsonify

from utils.decode_jwt import decode_jwt

from database.database import edit_username

edit_username_blueprint = Blueprint("edit_username", __name__, url_prefix="/api")

@edit_username_blueprint.route("/edit-username", methods=["POST"])
def edit_username_route():
    data = request.get_json() # read request as json

    # decode jwt and get user_id
    decoded_jwt = decode_jwt(current_app, request) # decode jwt
    user_id = decoded_jwt["user_id"] # get user_id from jwt

    # get new_username from request and send with user_id to database function
    new_username = data["newUsername"]
    edit_username(user_id, new_username)

    return jsonify({
        "error": False,
        "message": "Updated username successfully."
    }), 200
