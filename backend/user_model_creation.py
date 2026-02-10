import pytest
from your_app.models import User  # Replace 'your_app' with actual app name

class TestUserModelCreation:
    def test_valid_data(self):
        """Create valid user data"""
        user_data = {"name": "Test User", "email": "test@example.com"}
        user = User.objects.create(**user_data)
        assert user.name == user_data["name"]
        assert user.email == user_data["email"]

    def test_weak_password(self):
        """Test weak password validation"""
        user_data = {"name": "Test User", "password": "weak"}
        with pytest.raises(ValidationError) as exc:
            User.objects.create(**user_data)
        assert str(exc.value).lower() == "Password too weak"