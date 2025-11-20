from flask import Blueprint, jsonify

from database.database import get_user_blogs

get_user_blogs_blueprint = Blueprint("get_user_blogs", __name__, url_prefix="/api")

@get_user_blogs_blueprint.route("/get-user-blogs/<username>", methods=["GET"])
def get_user_blogs_route(username):

    # call db function to retrieve the blogs of this user
    print(username)
    blogs = get_user_blogs(username)
    return jsonify({
        "error": False,
        "message": f"Found blogs for {username}.",
        "blogs": blogs,
    }), 200