import os
from flask import Flask
from database.database import init_db
from dotenv import load_dotenv

from routes import register, login, create_blog, delete_blog

# initialise app
app = Flask(__name__)

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