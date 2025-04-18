
<<<<<<< Updated upstream
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
=======
def test_add(a, b):
    """Add two numbers."""
    return a + b

def test_subtract(a, b):
    """Subtract two numbers."""
    return a - b

def test_multiply(a, b):
    """Multiply two numbers."""
    return a * b

def test_divide(a, b):
>>>>>>> Stashed changes
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
