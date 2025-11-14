import psycopg2

from flask import current_app

conn = psycopg2.connect(database=current_app.config["PSQL_DATABASE_NAME"], user=current_app.config["PSQL_DATABASE_USER"], password=current_app.config["PSQL_DATABASE_PASSWORD"], host=current_app.config["PSQL_DATABASE_HOST"], port=current_app.config["PSQL_DATABASE_PORT"])

cur = conn.cursor()

def create_users_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            username VARCHAR(255),
            password VARCHAR(255)        
        );
    """)

    conn.commit()


def register_user(first_name, last_name, username, password):
    cur.execute("""
        INSERT INTO users (first_name, last_name, username, password)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, username, password))

    conn.commit()


def does_username_exist(username):
    cur.execute("""
        SELECT username FROM users
        WHERE username = (%s);
    """, (username,))

    username = cur.fetchone() # try to assign the username if it exists

    # if username already exists return True (it does exist) otherwise False, it doesnt
    if (username):
        return True
    else:
        return False


def get_user_info_for_login(username):
    cur.execute("""
        SELECT id, password FROM users 
        WHERE username = (%s);
    """, (username,))

    user = cur.fetchone()

    if not user: # username exists
        return {
            "id": user[0],
            "password": user[1]
        }
    else: # username doesnt exist
        return None
    

    
##
##  Blog database stuff below
##

def create_blogs_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS blogs (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            content VARCHAR(255),
            isPublished BOOLEAN,
            user_id INT,
            CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

    conn.commit()


def create_blog_return_id(title, content, user_id, is_published):
    cur.execute("""
        INSERT INTO blogs (title, content, isPublished, userId) 
        VALUES (%s, %s, %s, %s);
    """, (title, content, user_id, is_published))

    conn.commit()

    blog_id = cur.fetchone()

    return blog_id


def update_blog(title, content, blog_id, is_published):
    cur.execute("""
        UPDATE blogs
        SET title = (%s), content = (%s), isPublished = (%s)
        WHERE id = (%s);
    """, (title, content, is_published, blog_id))

    conn.commit()


def delete_blog(title, content, blog_id):
    cur.execute("""
        DELETE FROM blogs
        WHERE title = (%s) AND content = (%s) AND id = (%s);
    """, (title, content, blog_id))

    conn.commit()