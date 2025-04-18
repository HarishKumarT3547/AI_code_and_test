import pytest
from createUser import createUser  # Replace 'your_module' with the actual module name

def test_example():
    """Example test function."""
    assert True  # Replace with actual tests

def test_another_example():
    """Another example test function."""
    assert 1 + 1 == 2  # Replace with actual tests

def test_addition():
    """Test the addition of two numbers."""
    assert 2 + 3 == 5
    assert -1 + 1 == 0
    assert 0 + 0 == 0

def test_subtraction():
    """Test the subtraction of two numbers."""
    assert 5 - 3 == 2
    assert 0 - 1 == -1
    assert 10 - 10 == 0

def test_multiplication():
    """Test the multiplication of two numbers."""
    assert 3 * 7 == 21
    assert -1 * 1 == -1
    assert 0 * 100 == 0

def test_division():
    """Test the division of two numbers."""
    assert 10 / 2 == 5
    assert 1 / 2 == 0.5
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0

def test_string_concatenation():
    """Test string concatenation."""
    assert "Hello, " + "world!" == "Hello, world!"
    assert "foo" + "bar" == "foobar"

def test_list_operations():
    """Test list operations."""
    my_list = [1, 2, 3]
    my_list.append(4)
    assert my_list == [1, 2, 3, 4]
    assert my_list[0] == 1
    assert len(my_list) == 4

def test_dictionary_operations():
    """Test dictionary operations."""
    my_dict = {'a': 1, 'b': 2}
    my_dict['c'] = 3
    assert my_dict['c'] == 3
    assert len(my_dict) == 3
    assert 'b' in my_dict

def test_boolean_logic():
    """Test boolean logic."""
    assert True is True
    assert False is not True
    assert (1 == 1) and (2 == 2)
    assert (1 == 1) or (2 == 3)

def test_create_user_valid():
    """Test creating a user with valid data."""
    user = createUser(
        firstName="John",
        lastName="Doe",
        email="john.doe@example.com",
        password="securepassword",
        phone="1234567890",
        address="123 Main St",
        city="Anytown",
        state="CA",
        zipCode="12345",
        country="USA",
        dob="1990-01-01",
        gender="Male",
        occupation="Engineer"
    )
    assert user["firstName"] == "John"
    assert user["lastName"] == "Doe"
    assert user["email"] == "john.doe@example.com"
    assert user["phone"] == "1234567890"

def test_create_user_short_password():
    """Test creating a user with a short password."""
    response = createUser(
        firstName="Jane",
        lastName="Doe",
        email="jane.doe@example.com",
        password="short",
        phone="1234567890",
        address="456 Elm St",
        city="Othertown",
        state="NY",
        zipCode="54321",
        country="USA",
        dob="1992-02-02",
        gender="Female",
        occupation="Designer"
    )
    assert response == {"error": "Password too short"}

def test_create_user_invalid_phone():
    """Test creating a user with an invalid phone number."""
    response = createUser(
        firstName="Alice",
        lastName="Smith",
        email="alice.smith@example.com",
        password="validpassword",
        phone="12345",  # Invalid phone number
        address="789 Oak St",
        city="Sometown",
        state="TX",
        zipCode="67890",
        country="USA",
        dob="1985-03-03",
        gender="Female",
        occupation="Manager"
    )
    assert response == {"error": "Invalid phone number"}

# Additional tests can be added here for other scenarios 