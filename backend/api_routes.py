from flask import jsonify
from backend.auth import authenticate_user, register_user

def setup_auth_routes(app):
    @app.route('/login', methods=['POST'])
    def login():
        # This will be populated from auth.py's functions
        data = request.get_json()
        user = authenticate_user(data['email'], data['password'])
        if user:
            return jsonify({'token': generate_token(user)}), 200
        return jsonify({'error': 'Invalid credentials'}), 401

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if not check_email_exists(data['email']):
            new_user = register_user(data)
            return jsonify({'message': 'User created successfully'}), 201
        return jsonify({'error': 'Email already exists'}), 409