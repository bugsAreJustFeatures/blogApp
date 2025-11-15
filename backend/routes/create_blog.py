from flask import Blueprint, request, current_app, jsonify

from database.database import create_blog_return_id

from utils.decode_jwt import decode_jwt

create_blog_blueprint = Blueprint("create_blog", __name__, url_prefix="/api")

@create_blog_blueprint.route("/create-blog")
def create():

    data = request.get_json() # get request data as json

    title = data["formTitle"] # get title form input
    content = data["formContent"] # get content form input

    decoded_token = decode_jwt(current_app, request)

    # get user_id from token
    user_id = decoded_token["user_id"]

    # create blog 
    create_blog_return_id(title, content, user_id)

    return jsonify({
        "error": False,
        "message": "Blog created successfully."
    }), 201