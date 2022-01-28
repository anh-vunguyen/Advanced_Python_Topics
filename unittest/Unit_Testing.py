def add(x, y):
    """Add Function"""
    return x + y

def substract(x, y):
    """Substract Function"""
    return x - y

def  multiply(x, y):
    """Multiply function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y
