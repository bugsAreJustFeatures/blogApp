from flask import Blueprint, current_app, request, jsonify

from utils.decode_jwt import decode_jwt

from database.database import delete_blog

delete_blog_blueprint = Blueprint("delete_blog", __name__, url_prefix="/api")

@delete_blog_blueprint.route("/delete-blog", methods=["POST"])
def delete():
    data = request.get_json() # read request 

    blog_id = data["blog_id"] # get id of blog

    decoded_jwt = decode_jwt(current_app, request) # get jwt decoded

    user_id = decoded_jwt["user_id"] # get id of user

    # delete blog 
    delete_blog(user_id, blog_id)

    return jsonify({
        "error": False,
        "message": "Blog deleted successfully."
    }), 200





    