from flask import Blueprint, current_app, request, jsonify

from database.database import get_home_blogs

get_home_blogs_route_blueprint = Blueprint("home", __name__, url_prefix="/api")

@get_home_blogs_route_blueprint.route("/get-home-blogs", methods=["GET"])
def get_home_blogs_route():

    # call db to get home blogs - this returns 10
    home_blogs = get_home_blogs()
    
    return jsonify({
        "error": False,
        "message": "Blogs fetched successfully.",
        "blogs": home_blogs
    }), 200