from database.database import get_username_via_id

def get_username(user_id):
    # get username via database function
    username = get_username_via_id(user_id)
    
    return username