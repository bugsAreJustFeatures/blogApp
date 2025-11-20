from flask import jsonify

from utils.is_jwt_valid import is_jwt_valid
from utils.get_username import get_username
from utils.decode_jwt import decode_jwt

def is_self_search(current_app, request, username):

    jwt_is_valid = is_jwt_valid(current_app, request) # check if jwt is valid

    if not jwt_is_valid: # if its not return 401
        return jsonify({
            "error": True,
            "message": "JWT was invalid."
        }), 401
    
    # get user_id from jwt
    decoded_jwt = decode_jwt(current_app, request)
    user_id = decoded_jwt["user_id"]

    # get the username of the account doing the search for the blogs
    username_doing_search = get_username(user_id)[0] # returns a tuple

    # check if the user is searching themselves
    if not username == username_doing_search:
        return False
    else:
        # user is searching themselves
        return True

