from flask import Blueprint, current_app, request, jsonify

from utils.decode_jwt import decode_jwt

from database.database import edit_blog

edit_blog_blueprint = Blueprint("edit", __name__, url_prefix="/api")

@edit_blog_blueprint.route("/", methods=["POST"])
def edit():
    data = request.get_json() # read request as json

    title = data["title"] # get blog title from request
    content = data["content"] # get blog content from request
    blog_id = data["blog_id"] # get blog id from request
    is_published = data["is_published"] # get is_published from request

    # edit blog in db
    edit_blog(title, content, blog_id, is_published)

    return jsonify({
        "error": False,
        "message": "Edited blog successfully."
    }), 200
