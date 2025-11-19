from flask import Blueprint, current_app, jsonify, request

from database.database import get_blog

get_blog_blueprint = Blueprint("get", __name__, url_prefix="/api")

@get_blog_blueprint.route("/get-blog/<blog_id>", methods=["GET"])
def get_blog_route(blog_id):
    blog = get_blog(blog_id) # get blog from db

    if not blog: # blog returned None so no blog could be found
        return jsonify({
            "error": True,
            "message": "No blog found."
        }), 200
    
    # get blog details
    blog_title = blog[0]
    blog_content = blog[1]
    blog_is_published = blog[2]
    blog_created_on = blog[3]
    blog_username = blog[4]

    return jsonify({
        "error": False,
        "message": "Found blog successfully.",
        "title": blog_title,
        "content": blog_content,
        "is_published": blog_is_published,
        "date": blog_created_on,
        "username": blog_username
    }), 200


