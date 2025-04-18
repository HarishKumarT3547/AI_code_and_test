import pytest
from example import add, subtract, multiply, divide  # Import the functions from your example.py file

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(10, 10) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 7) == 21
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(1, 2) == 0.5
    with pytest.raises(ValueError):
        divide(1, 0)
