def create_test_user(email, password):
    # Simulate creating a new user
    return {
        "email": email,
        "password": password,
        "username": email.split("@")[0],
    }

test_users = [
    create_test_user("user1@example.com", "Password123!"),
    create_test_user("user2@example.com", "weakpassword"),
    create_test_user("invalid_email", "strong_password"),
    create_test_user("user3@example.com", ""),  # Empty password
    create_test_user("user4@example.com", None),  # Invalid data type
]

# filename.py

def test_automated_login_success():
    # Arrange
    user_data = next(test_users)
    
    # Act
    login_response = automated_login(user_data["email"], user_data["password"])
    
    # Assert
    assert login_response.status_code == 200
    assert "login successful" in login_response.content.decode("utf-8")

def test_automated_login_failure():
    # Arrange
    user_data = next(test_users)
    
    # Act
    login_response = automated_login(user_data["email"], user_data["weakpassword"])
    
    # Assert
    assert login_response.status_code == 401