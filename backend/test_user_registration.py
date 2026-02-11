import pytest
from autodev import app, models

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_successful_registration(client):
    user_data = {"email": "test@example.com", "password": "SecurePass123!"}
    response = client.post("/register", json=user_data)
    assert response.status_code == 201
    assert models.User.query.count() == 1

def test_weak_password(client):
    user_data = {"email": "test@example.com", "password": "123"}
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert "password too weak" in response.json()["error"]

def test_empty_fields(client):
    user_data = {}
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    for field, error_message in {"email": "Email is required", "password": "Password is required"}:
        assert f"{field} validation error" in str(response.json()["error"])

def test_duplicate_email(client):
    user_data = {"email": "test@example.com"}
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert "Email already exists" in response.json()["error"]

def test_invalid_email(client):
    user_data = {"email": "test@"}
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert "Invalid email" in response.json()["error"]