from flask import session, g
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False

    if not check_password_hash(user.password_hash, password):
        return False

    session['user_id'] = user.id
    g.user = user
    return True

def get_current_user():
    user_id = session.get('user_id')
    if not user_id:
        return None

    user = User.query.get(user_id)
    return user