from backend.database import db
import hashlib
import secrets

class RegisterUserService:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def hash_password(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def generate_api_key(self):
        return secrets.token_hex(16)

    async def register_user(self):
        # Hash password and generate API key
        hashed_password = self.hash_password()
        api_key = self.generate_api_key()

        # Create user entry in database
        user_entry = User(username=self.username, email=self.email, password=hashed_password, api_key=api_key)
        db.session.add(user_entry)

        return user_entry

class User:
    def __init__(self, username, email, password, api_key):
        self.username = username
        self.email = email
        self.password = password
        self.api_key = api_key