from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = self._hash_password(password)

    @staticmethod
    def _hash_password(password):
        # Using bcrypt for password hashing
        import bcrypt
        return bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        # Verifying password using bcrypt
        return bcrypt.checkpw(str(password).encode('utf-8'), self.password_hash)

# Create a session maker
Session = sessionmaker(bind=Base.metadata)
session = Session()

# Import validation schema
from backend.validators import UserValidator

# Define the validation schema for User model
class UserValidator:
    def validate(self, user):
        errors = []
        if not user.username:
            errors.append("Username is required")
        if not user.email:
            errors.append("Email is required")
        return errors