import requests
import pytest

def send_request(url, data):
    """Send a POST request to the specified URL with the provided data."""
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def test_register_valid_data():
    """Test registration with valid user data."""
    url = "/register"
    data = {
        "email": "test@example.com",
        "password": "SecurePass123!"
    }
    result = send_request(url, data)
    assert result is not None
    assert result["status"] == "success"
    assert result["user_id"] is not None

def test_register_weak_password():
    """Test registration with weak user data."""
    url = "/register"
    data = {
        "email": "test@example.com",
        "password": "123"
    }
    result = send_request(url, data)
    assert result is not None
    assert result["status"] == "failure"
    assert "password too weak" in result["error"]

def test_register_missing_data():
    """Test registration with missing user data."""
    url = "/register"
    data = {
        "email": "",
        "password": ""
    }
    result = send_request(url, data)
    assert result is not None
    assert result["status"] == "failure"
    assert "required field(s) are missing" in result["error"]

def test_register_invalid_input_types():
    """Test registration with invalid input types."""
    url = "/register"
    data = {
        "email": "",
        "password": 123
    }
    result = send_request(url, data)
    assert result is not None
    assert result["status"] == "failure"
    assert "required field(s) have incorrect type" in result["error"]