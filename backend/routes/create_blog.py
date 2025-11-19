from flask import Blueprint, request, current_app, jsonify

from database.database import create_blog_return_id

from utils.decode_jwt import decode_jwt
from backend.utils.is_jwt_valid import is_jwt_valid

create_blog_blueprint = Blueprint("create_blog", __name__, url_prefix="/api")

@create_blog_blueprint.route("/create-blog", methods=["POST"])
def create():

    data = request.get_json() # get request data as json

    let_user_through = is_jwt_valid(current_app, request) # check jwt

    # check if jwt is valid
    if not let_user_through: # is not valid
        return jsonify({
            "error": True,
            "message": "JWT is invalid."
        }), 401

    title = data["title"] # get title form input
    content = data["content"] # get content form input
    is_published = data["isPublished"] # get published status

    # get user_id from token after decoding it                   
    decoded_token = decode_jwt(current_app, request)
    user_id = decoded_token["user_id"]

    # create blog 
    blog_id = create_blog_return_id(title, content, is_published, user_id)

    return jsonify({
        "error": False,
        "message": "Blog created successfully.",
        "blog_id": blog_id
    }), 201