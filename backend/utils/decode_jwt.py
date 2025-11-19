import jwt

def decode_jwt(current_app, request):
    auth_header = request.headers["Authorization"] # get jwt from Authorization header
    bearer_token = auth_header.split(" ") # comes as "Bearer [JWT]"
    token = bearer_token[1] # gets the [JWT] part

    # check there is a token along with the bearer
    if token == "null": # this is null because its in json (javascript)
        return None

    # decode jwt to get user_id
    decoded_token = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])

    return decoded_token