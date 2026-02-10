from backend.database import User

def get_users(limit=10, offset=0):
    users = User.query.offset(offset).limit(limit)
    return [user.to_dict() for user in users]