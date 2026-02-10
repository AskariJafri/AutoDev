from flask import Blueprint, request, jsonify
from auth import authenticate, get_current_user
from models import User

user_api = Blueprint('user', __name__)

@user_api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        authenticate(email, password)
        return jsonify({'message': 'Logged in successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@user_api.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user = User.validate(email, password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@user_api.route('/logout')
def logout():
    session.pop('user_id', None)
    g.user = None
    return jsonify({'message': 'Logged out successfully'}), 200