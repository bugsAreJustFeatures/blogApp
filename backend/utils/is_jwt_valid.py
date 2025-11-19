from flask import jsonify

from utils import decode_jwt 

from database.database import does_user_id_exist

import time

# function that takes in a jwt, if it exists, and checks that data inside is valid
def is_jwt_valid(current_app, request):

    # first, check if there is an Authorization otherwise just return 401 straight away rather than checking
    if not request.headers["Authorization"]:
        return jsonify({
            "error": True,
            "message": "No 'Authorization' header.",
        }), 40

    # call decode_jwt to try to check if theres a user_id in it and that the exp date hasnt passed
    decoded_jwt = decode_jwt.decode_jwt(current_app, request)

    # make sure both current time and the exp time is stored in unix time, this is just every second since 1970 (also called epoch time)
    current_time = int(time.time()) # this is the current time stored in unix
    exp_time = decoded_jwt["exp"] # get my exp time that i stored in my jwt

    # compare the times, if current is larger than its expired, otherwise its valid
    if current_time > exp_time: # invalid and expired
        return True
    
    # check that the jwt contains a the correct user_id
    valid_user_id = does_user_id_exist(decoded_jwt["user_id"])

    # return final response
    if not valid_user_id:
        return False
    else:
        return True


    


