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
            password VARCHAR(255),    
            created_on TIMESTAMP DEFAULT NOW() 
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS blogs (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            content VARCHAR(255),
            is_published BOOLEAN,
            created_on TIMESTAMP DEFAULT NOW(),
            user_id INT,
            CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

    # cur.execute("""
    #     INSERT INTO users (first_name, last_name, username, password)
    #     VALUES ('user1', 'user1', 'username1', 'myPassword');
    # """)

    # cur.execute("""
    #     INSERT INTO blogs (title, content, is_published, user_id)
    #     VALUES ('blog1', 'blog1', true, 1)
    # """)

    # cur.execute("""
    #     INSERT INTO blogs (title, content, is_published, user_id)
    #     VALUES ('new blog', 'this is my new blog', true, 4)
    # """)
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


# check if a user with an id exists
def does_user_id_exist(user_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT username FROM users
        WHERE id = (%s);
    """, (user_id,))

    user = cur.fetchone() # try to assign the user if it exists

    # if user exists return True otherwise False, it doesnt
    if (user):
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

    if user: # username exists
        return {
            "id": user[0],
            "password": user[1]
        }
    else: # username doesnt exist
        return None
    

# edit username 
def edit_username(user_id, new_username):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET username = (%s)
        WHERE id = (%s);
    """, (new_username, user_id))

    conn.commit()


# edit first name
def edit_first_name(user_id, new_first_name):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET first_name = (%s)
        WHERE id = (%s);
    """, (new_first_name, user_id))

    conn.commit()


# edit last name
def edit_last_name(user_id, new_last_name):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET last_name = (%s)
        WHERE id = (%s);
    """, (new_last_name, user_id))

    conn.commit()

# edit both names
def edit_name(user_id, new_first_name, new_last_name):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET first_name = (%s), last_name = (%s)
        WHERE id = (%s);
    """, (new_first_name, new_last_name, user_id))

    conn.commit()


# edit password
def edit_password(user_id, new_password):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET password = (%s)
        WHERE id = (%s);
    """, (new_password, user_id))

    conn.commit()

# delete user account
def delete_account(user_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM users 
        WHERE id = (%s);
    """, (user_id,))

    conn.commit()
    
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
        SELECT blogs.title, blogs.content, blogs.is_published, blogs.created_on, users.username FROM blogs
        LEFT JOIN users
        ON blogs.user_id = users.id
        WHERE blogs.id = (%s);
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


# get home blogs - this is just a set amount of blogs in desc order (for now 10 and if i want to i can implement pages where each page sends another request and gets another 10 for example)
def get_home_blogs():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT blogs.id, blogs.title, blogs.content, blogs.created_on, users.username FROM blogs
        LEFT JOIN users
        ON blogs.user_id = users.id
        WHERE is_published = true
        ORDER BY created_on DESC
        LIMIT 10;
    """)

    home_blogs = cur.fetchall()

    return home_blogs


# get blogs of a specfic user
def get_user_blogs(username):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT id FROM users
        WHERE username = (%s);
    """, (username,))

    user_id = cur.fetchone()

    cur.execute("""
        SELECT blogs.id, blogs.title, blogs.content, blogs.created_on, users.username FROM blogs
        LEFT JOIN users
        ON blogs.user_id = users.id
        WHERE blogs.user_id = (%s)
        ORDER BY created_on DESC
        LIMIT 10;
    """, (user_id,))

    user_blogs = cur.fetchall()

    return user_blogs


