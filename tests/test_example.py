import pytest

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