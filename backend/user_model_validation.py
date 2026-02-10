import pytest
from your_app.models import User  # Replace 'your_app' with actual app name

class TestUserModelValidation:
    def test_required_fields(self):
        """Validate required fields are enforced"""
        user_data = {"name": "Test User", "email": "test@example.com"}
        with pytest.raises(ValidationError) as exc:
            User.objects.create(**user_data)
        assert str(exc.value).lower() == "name and email are required"

    def test_email_format(self):
        """Validate email format"""
        user_data = {"name": "Test User", "email": "invalid_email"}
        with pytest.raises(ValidationError) as exc:
            User.objects.create(**user_data)
        assert str(exc.value).lower() == "Invalid email address"