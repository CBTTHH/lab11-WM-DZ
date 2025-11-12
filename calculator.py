# https://github.com/CBTTHH/lab11-WM-DZ.git
# Partner 1: William Munro
# Partner 2: David Zou


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("Input must be a number.")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Inputs must be numbers.")

def add(a, b): 
    return (a+b)

def sub(a,b):
    return (a-b)

def mul(a,b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    result = b / a
    return result
        # print("Error: Division by zero is not allowed.")

def log(a, b):
    try:
        result = math.log(b,a)
        return result
    except:
        raise ValueError
    
def exp(a,b):
    return (a**b)


