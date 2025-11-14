import os
from flask import Flask
from database.database import create_users_table, create_blogs_table
from dotenv import load_dotenv

from routes import register, login

app = Flask(__name__)
app.config["PSQL_DATABASE_NAME"] = os.getenv("DATABASE_NAME")
app.config["PSQL_DATABASE_USER"] = os.getenv("DATABASE_USER")
app.config["PSQL_DATABASE_PASSWORD"] = os.getenv("DATABASE_PASSWORD")
app.config["PSQL_DATABASE_HOST"] = os.getenv("DATABASE_HOST")
app.config["PSQL_DATABASE_PORT"] = os.getenv("DATABASE_PORT")


create_users_table()
create_blogs_table()

app.register_blueprint(register.register_route_blueprint)
app.register_blueprint(login.login_route_blueprint)