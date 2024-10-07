# Control Flow Statements
# src/basics/control_flow.py

def control_flow_demo(value):
    # Example of if, elif, else in Python (similar to Java's if-else structure)
    if value > 10:
        result = "Value is greater than 10"
    elif value == 10:
        result = "Value is equal to 10"
    else:
        result = "Value is less than 10"

    # Example of a for loop (more concise compared to Java's for-each loop)
    for i in range(5):  # Iterates from 0 to 4
        print(f"Iteration {i}")

    # Example of a while loop
    while value > 0:
        print(f"Value: {value}")
        value -= 1

    return result

def nested_loops_demo():
    # Example of nested loops
    for i in range(3):
        for j in range(2):
            print(f"i: {i}, j: {j}")

if __name__ == "__main__":
    print(control_flow_demo(12))
    nested_loops_demo()
