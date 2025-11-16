import os
from flask import Flask, request
from database.database import init_db
from dotenv import load_dotenv

from routes import register, login, create_blog, get_blog, edit_blog, delete_blog, edit_username, edit_name, delete_account, get_home_blogs

# initialise app
app = Flask(__name__)


# use this to forge a jwt to test routes - DELETE IN PRODUCTION
FAKE_JWT = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJleHAiOjE3NjM1NTEyNTR9.Q8TBDyZ7Fh4MHuAy4xDEcS80LgsQy_EGsyHkubbtomE"
@app.before_request
def inject_fake_jwt():
    # Werkzeug request headers are immutable, so we modify the environ instead
    request.environ["HTTP_AUTHORIZATION"] = FAKE_JWT

# connection string variables
app.config["PSQL_DATABASE_NAME"] = os.getenv("DATABASE_NAME")
app.config["PSQL_DATABASE_USER"] = os.getenv("DATABASE_USER")
app.config["PSQL_DATABASE_PASSWORD"] = os.getenv("DATABASE_PASSWORD")
app.config["PSQL_DATABASE_HOST"] = os.getenv("DATABASE_HOST")
app.config["PSQL_DATABASE_PORT"] = os.getenv("DATABASE_PORT")

# jwt variable
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# run this so it waits for application to be established and not run outside of context
with app.app_context():
    init_db()

# register blueprints
app.register_blueprint(register.register_blueprint)
app.register_blueprint(login.login_blueprint)
app.register_blueprint(create_blog.create_blog_blueprint)
app.register_blueprint(delete_blog.delete_blog_blueprint)
app.register_blueprint(get_blog.get_blog_blueprint)
app.register_blueprint(edit_blog.edit_blog_blueprint)
app.register_blueprint(edit_username.edit_username_blueprint)
app.register_blueprint(edit_name.edit_name_blueprint)
app.register_blueprint(delete_account.delete_account_blueprint)
app.register_blueprint(get_home_blogs.get_home_blogs_route_blueprint)