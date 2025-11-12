"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return (a+b)

def sub(a,b):
    return (a-b)

def mul(a,b):
    return a*b

def div(a, b):
    try:
        result = b / a
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def log(a, b):
    try:
        result = math.log(b, a)
        return result
    except ValueError:
        print("Error: log() arguments must be positive and base cannot be 1.")
        return None
def exp(a,b):
    return (a**b)


