import pytest
from your_app.models import User  # Import User model from your app

def test_empty_email():
    """Test email is required"""
    user_data = {"password": "SecurePass123!"}
    with pytest.raises(ValidationError) as exc:
        User.objects.create(**user_data)
    assert "email" in str(exc.value).lower()

def test_empty_password():
    """Test password is required"""
    user_data = {"email": "test@example.com"}
    with pytest.raises(ValidationError) as exc:
        User.objects.create(**user_data)
    assert "password" in str(exc.value).lower()

def test_invalid_email_format():
    """Test email format validation"""
    user_data = {"email": "invalid-email", "password": "SecurePass123!"}
    with pytest.raises(ValidationError) as exc:
        User.objects.create(**user_data)
    assert "email" in str(exc.value).lower()

def test_password_strength():
    """Test password strength requirements"""
    weak_password = "weak"
    strong_password = "StrongPassword123!"
    user_data = {"password": weak_password}
    with pytest.raises(ValidationError) as exc:
        User.objects.create(**user_data)
    assert "password" in str(exc.value).lower()

def test_username_validation():
    """Test username length and format validation"""
    short_username = "ab"
    long_username = "a".join([chr(i) for i in range(256)])
    user_data = {"username": short_username}
    with pytest.raises(ValidationError) as exc:
        User.objects.create(**user_data)
    assert "username" in str(exc.value).lower()