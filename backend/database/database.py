import psycopg2

from flask import current_app

# need to have get_conn() function otherwise it runs on import and causes a runtime error since it tries to work outside of applciation context. 
# I am pretty sure this just means, "The current_app will try to be read whilst its still being established since i have imported it into the app file"
# so instead it establishes the files and read all, AND THEN, it will call the functions after reading them

# get connection string and has to be func because of reason above ^^^
def get_conn():
    database_name = current_app.config["PSQL_DATABASE_NAME"]
    user = current_app.config["PSQL_DATABASE_USER"]
    password = current_app.config["PSQL_DATABASE_PASSWORD"]
    host = current_app.config["PSQL_DATABASE_HOST"]
    port=current_app.config["PSQL_DATABASE_PORT"]

    conn = psycopg2.connect(f"postgresql://{user}:{password}@{host}:{port}/{database_name}")

    return conn

# func for initialising the db on app run (if it doesnt exist already)
def init_db():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            username VARCHAR(255),
            password VARCHAR(255)        
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS blogs (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            content VARCHAR(255),
            is_published BOOLEAN,
            user_id INT,
            CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

    conn.commit()


# registers user in users table
def register_user(first_name, last_name, username, password):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users (first_name, last_name, username, password)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, username, password))

    conn.commit()


# checks if username exists
def does_username_exist(username):
    conn = get_conn()
    cur = conn.cursor()

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


# gets user info for login, which is their password (to check they entered it correctly) and id, to store in jwt
def get_user_info_for_login(username):
    conn = get_conn()
    cur = conn.cursor()

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


# create a blog in the blogs table
def create_blog_return_id(title, content, is_published: bool, user_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO blogs (title, content, is_published, user_id) 
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (title, content, is_published, user_id ))

    conn.commit()

    blog_id = cur.fetchone()

    return blog_id


# get blog details to display 
def get_blog(blog_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT title, content, is_published, user_id FROM blogs
        WHERE id = (%s);
    """, (blog_id,))

    blog_details = cur.fetchone()

    return blog_details


# edits blog details that is stored in db
def edit_blog(title, content, blog_id, is_published: bool):
    conn = get_conn()
    cur = conn.cursor()
    
    cur.execute("""
        UPDATE blogs
        SET title = (%s), content = (%s), isPublished = (%s)
        WHERE id = (%s);
    """, (title, content, is_published, blog_id))

    conn.commit()


# delete a blog stored in db
def delete_blog(user_id, blog_id):
    conn = get_conn()
    cur = conn.cursor()
    
    cur.execute("""
        DELETE FROM blogs
        WHERE user_id = (%s) AND id = (%s);
    """, (user_id, blog_id))

    conn.commit()

