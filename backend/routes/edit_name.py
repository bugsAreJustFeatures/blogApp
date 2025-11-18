from flask import Blueprint, current_app, request, jsonify

from utils.decode_jwt import decode_jwt

from database.database import edit_first_name, edit_last_name, edit_name

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

    # check that at least one new name has been inputted 
    if len(new_first_name) == 0 and len(new_last_name) == 0:
        return jsonify({
            "error": True,
            "message": "No name was entered."
        }), 200
    
    # check which name the user wants to update
    if len(new_first_name) > 0 and len(new_last_name) == 0: # update first name
        edit_first_name(user_id, new_first_name)

        return jsonify({
            "error": False,
            "message": "First name updated successfully."
        }), 200

    elif len(new_first_name) == 0 and len(new_last_name) > 0: # update last name
        edit_last_name(user_id, new_last_name)

        return jsonify({
            "error": False,
            "message": "Last name updated successfully."
        }), 200

    else: # both names want updating
        edit_name(user_id, new_first_name, new_last_name)

        return jsonify({
            "error": False,
            "message": "Name updated successfully."
        }), 200