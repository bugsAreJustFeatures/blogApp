from flask import Blueprint, current_app, request, jsonify

from utils.decode_jwt import decode_jwt

from database.database import edit_name

edit_name_blueprint = Blueprint("edit_name", __name__, url_prefix="/api")

@edit_name_blueprint.route("/edit-name", methods=["POST"])
def edit_name_route():
    data = request.get_json() # read request as json

    # decode jwt and get user_id
    decoded_jwt = decode_jwt(current_app, request)
    user_id = decoded_jwt["user_id"]

    # get new name from request edit name
    new_first_name = data["newFirstName"]
    new_last_name = data["newLastName"]

    edit_name(user_id, new_first_name, new_last_name)

    return jsonify({
        "error": False,
        "message": "Name updated successfully."
    }), 200