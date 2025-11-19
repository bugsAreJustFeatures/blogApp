import jwt

def decode_jwt(current_app, request):
    auth_header = request.headers["Authorization"] # get jwt from Authorization header
    bearer_token = auth_header.split(" ") # comes as "Bearer [JWT]"
    token = bearer_token[1] # gets the [JWT] part

    # decode jwt to get user_id
    decoded_token = jwt.decode(token,current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])

    return decoded_token