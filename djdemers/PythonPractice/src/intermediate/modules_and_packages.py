# src/intermediate/modules_and_packages.py

import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

def calculate_square_root(value):
    return math.sqrt(value)

def calculate_logarithm(value, base=math.e):
    return math.log(value, base)

if __name__ == "__main__":
    print(calculate_circle_area(5))
    print(calculate_square_root(16))
    print(calculate_logarithm(100,10))
