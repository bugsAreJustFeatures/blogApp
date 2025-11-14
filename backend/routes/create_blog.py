from flask import Blueprint, request

from database import database as db

create_blog = Blueprint("create_blog", __name__, url_prefix="/api")

@create_blog.route("/create-blog")
def create():
    data = request.get_json()

    title = data["formTitle"]
    content = data["formContent"]

    # create blog 
    # db.create_blog_return_id(title, content, user_id)