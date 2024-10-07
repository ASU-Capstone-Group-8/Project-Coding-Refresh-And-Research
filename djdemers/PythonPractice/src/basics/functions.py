# Basic Functions
# src/basics/functions.py

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def add_numbers(a, b=5):
    return a + b

def factorial(n):
    # Example of a recursive function
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(greet_user("David"))
    print(add_numbers(3))
    print(add_numbers(3, 10))
    print(factorial(5))


