import pytest
from auto_dev.models import User, Order

def test_create_user():
    """Create a new user with valid data"""
    user_data = {"email": "test@example.com", "password": "SecurePass123!"}
    user = create_test_user(user_data)
    assert user.email == user_data["email"]
    assert user.password != ""

def test_update_user_profile():
    """Update an existing user's profile"""
    user_data = {"name": "John Doe", "phone": "+1 123 456 7890"}
    update_user_profile(1, user_data)
    user = get_user(1)
    assert user.name == user_data["name"]
    assert user.phone == user_data["phone"]

def test_retrieve_user_profile():
    """Retrieve a user's profile"""
    user_data = {"email": "test@example.com", "password": "SecurePass123!"}
    create_test_user(user_data)
    user = get_user(1)
    assert user.email == user_data["email"]
    assert user.password != ""

def test_delete_user_account():
    """Delete a user's account"""
    user_data = {"email": "test@example.com", "password": "SecurePass123!"}
    create_test_user(user_data)
    delete_user_account(1)
    with pytest.raises(User.DoesNotExist):
        get_user(1)

# filename.py

import pytest
from auto_dev.models import User, Order

def test_order_history():
    """Retrieve a user's order history"""
    # Create two orders for the same user
    create_test_orders([123, 456], 1)
    # Retrieve the user's order history
    orders = get_user_order_history(1)
    assert len(orders) == 2

def test_delete_order():
    """Delete an order from a user's account"""
    # Create two orders for the same user
    create_test_orders([123, 456], 1)
    # Delete one of the orders
    delete_order(123, 1)
    # Retrieve the updated order history
    orders = get_user_order_history(1)
    assert len(orders) == 1

# filename.py

import pytest
from auto_dev.models import User, Order

def test_create_order():
    """Create a new order"""
    # Create a new user
    create_test_user({"email": "test@example.com", "password": "SecurePass123!"})
    # Create a new order for the same user
    create_new_order(1)
    # Retrieve the created order
    order = get_order(123)
    assert order.user_id == 1

def test_update_order():
    """Update an existing order"""
    # Create a new user
    create_test_user({"email": "test@example.com", "password": "SecurePass123!"})
    # Create a new order for the same user
    create_new_order(1)
    # Update one of the fields of the order
    update_order(123, {"status": "shipped"})
    # Retrieve the updated order
    order = get_order(123)
    assert order.status == "shipped"

# filename.py

import pytest
from auto_dev.models import User, Order

def test_delete_order():
    """Delete an order"""
    # Create a new user
    create_test_user({"email": "test@example.com", "password": "SecurePass123!"})
    # Create a new order for the same user
    create_new_order(1)
    # Delete the order
    delete_order(123)
    # Retrieve the updated order history
    orders = get_user_order_history(1)
    assert len(orders) == 0