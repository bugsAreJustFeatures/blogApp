from flask import Flask

from routes import register, login

from database.database import create_users_table, create_blogs_table

app = Flask(__name__)

create_users_table()
create_blogs_table()

app.register_blueprint(register.register_route_blueprint)
app.register_blueprint(login.login_route_blueprint)