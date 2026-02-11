import unittest
from yourapp.models import User  # Replace 'yourapp' with your actual app name
from yourapp.utils import validate_user_input  # Replace 'yourapp' with your actual app name

class TestUserModelValidation(unittest.TestCase):
    def test_valid_user_input(self):
        user_data = {
            "email": "test@example.com",
            "password": "SecurePass123!"
        }
        result = validate_user_input(user_data)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["user_id"], 1)  # Replace with actual user ID

    def test_required_fields(self):
        user_data = {
            "email": "",
            "password": "SecurePass123!"
        }
        result = validate_user_input(user_data)
        self.assertEqual(result["status"], "error")
        self.assertIn("email is required", str(result))

    def test_email_format(self):
        user_data = {
            "email": "invalid_email"
        }
        result = validate_user_input(user_data)
        self.assertEqual(result["status"], "error")
        self.assertIn("Invalid email format", str(result))