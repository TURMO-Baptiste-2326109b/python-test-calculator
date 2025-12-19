def add(a, b):
    checkinputs(a, b)
    return a + b

def subtract(a, b):
    checkinputs(a, b)
    return a - b

def multiply(a, b):
    checkinputs(a, b)
    return a * b

def divide(a, b):
    checkinputs(a, b)
    return a / b

def checkinputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be either int or float!")
