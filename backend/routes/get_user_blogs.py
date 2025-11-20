from flask import Blueprint, current_app, request, jsonify

from database.database import get_user_blogs, get_user_blogs_unpublished

from utils.is_self_search import is_self_search

get_user_blogs_blueprint = Blueprint("get_user_blogs", __name__, url_prefix="/api")

@get_user_blogs_blueprint.route("/get-user-blogs/<username>", methods=["GET"])
def get_user_blogs_route(username):

    # check if the user is self searching
    self_search = is_self_search(current_app, request, username)

    if self_search:
        # call db function to retrieve the blogs of this user
        blogs = get_user_blogs_unpublished(username)
    else:
        # call db function to retrieve the blogs of another user
        blogs = get_user_blogs(username)

    # return to frontend
    return jsonify({
        "error": False,
        "message": f"Found blogs for {username}.",
        "selfSearch": self_search,
        "blogs": blogs,
    }), 200