from sqlalchemy import Column, String, Email, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from validators import validate_email

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255))
    is_active = Column(Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def validate(cls, email, password):
        user = cls.query.filter_by(email=email).first()
        if not user:
            raise ValueError("Invalid email or password")

        if not validate_email(email):
            raise ValueError("Invalid email format")

        if not user.check_password(password):
            raise ValueError("Invalid password")