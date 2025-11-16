from flask import Blueprint, current_app, request, jsonify

from database.database import delete_account

from utils.decode_jwt import decode_jwt

delete_account_blueprint = Blueprint("delete_account", __name__, url_prefix="/api")

@delete_account_blueprint.route("/delete-account", methods=["POST"])
def delete_account_route():
    data = request.get_json() # read request as json

    # decode jwt and get user_id
    decoded_jwt = decode_jwt(current_app, request)
    user_id = decoded_jwt["user_id"]

    # delete account
    delete_account(user_id)

    return jsonify({
        "error": False,
        "message": "Account deleted successfully."
    }), 200