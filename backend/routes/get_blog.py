from flask import Blueprint, current_app, jsonify, request

from database.database import get_blog

get_blog_blueprint = Blueprint("get", __name__, url_prefix="/api")

@get_blog_blueprint.route("/get-blog", methods=["GET"])
def get_blog():
    data = request.get_json() # read request as json

    blog_id = data["blog_id"] # get blog_id from request

    blog = get_blog(blog_id) # get blog from db

    if not blog: # blog returned None so no blog could be found
        return jsonify({
            "error": True,
            "message": "No blog found."
        }), 200
    
    # get blog details
    blog_title = blog["title"]
    blog_content = blog["content"]
    blog_is_published = blog["is_published"]
    blog_user_id = blog["user_id"]

    return jsonify({
        "error": False,
        "message": "Found blog successfully.",
        "blog_tile": blog_title,
        "blog_content": blog_content,
        "blog_is_published": blog_is_published,
        "blog_user_id": blog_user_id
    }), 200


