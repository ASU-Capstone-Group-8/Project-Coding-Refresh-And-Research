# src/basics/helloWorld.py
import sys



# This defines the main function of the program.
# A function in Python is defined using the "def" keyword, followed by the function name and parentheses.
# The parentheses can contain parameters, but here it is empty since this function doesn't take any inputs.
def main():
    # This is the body of the main function.
    # "print" is a built-in Python function that outputs the specified message to the console.
    # In this case, the message "Hello, World!" is being passed as an argument to the print function.
    # When executed, this will display the text "Hello, World!" in the console.
    print("Hello, World!")
    sys.exit(0) # Exit the program after printing

# This part checks if the Python script is being run directly (not imported as a module).
# "__name__" is a special built-in variable in Python that holds the name of the module currently being executed.
# If the script is run directly by the user, the "__name__" variable will be set to the string "__main__".
# The condition "if __name__ == '__main__':" is checking if this script is the main script being run.
# If this condition is true, it means that this script is being run directly (not imported as a module into another script).
if __name__ == "__main__":
    # If the script is being run directly, this line will be executed.
    # The "main()" function is called here, which will trigger the code inside the "main" function to run.
    main()

