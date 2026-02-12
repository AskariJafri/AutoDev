from django.contrib.auth.models import User
from backend.database import db_session
from backend.models import *
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
import logging

logger = logging.getLogger(__name__)

def register_user(email, password, username):
    """Register new user with email, password, and username."""
    try:
        # Validate inputs
        if not all([email, password, username]):
            raise ValueError("All fields are required")
            
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            raise ValueError("Email already registered")

        # Create user
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        
        # Generate token for activation
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(str(user.id).encode())
        
        # Send confirmation email
        send_confirmation_email(email, username, uid, token)
        
        return {"status": "success", "message": "User registered successfully!"}
        
    except Exception as e:
        logger.error(f"Registration failed: {str(e)}")
        raise

def send_confirmation_email(email, username, uid, token):
    """Send confirmation email to newly registered user."""
    subject = f'Welcome {username}! Confirm your email.'
    message = f'''
        Dear {username},
        Please confirm your email by clicking on the link below:
        http://localhost:8000/confirm-email/{uid}/{token}
        If you didn't initiate this registration, you can safely ignore this email.
    '''
    send_mail(subject, message, 'admin@example.com', [email])

# Example usage
if __name__ == "__main__":
    # Testing registration
    try:
        test_user = register_user(
            email='test@example.com',
            password='securepassword123',
            username='testuser'
        )
        print(test_user)
    except Exception as e:
        print(f"Error during testing: {str(e)}")