# src/basics/variables.py

# Example Python Script for Variables

# In Python, functions are defined using the def keyword, followed by the function name and parentheses.
# This is similar to how Java uses void or a return type for function definitions, but Python doesn't require
# specifying the return type.

def display_variables():
    # In Python, variables do not require explicit type declarations, unlike Java where types
    # must be declared. Python determines the type based on the value assigned.

    # Example of variable assignment (without type declaration):
    name = "David"
    age = 37
    height = 6.4
    is_student = True

    # Python automatically manages data types at runtime. Java would require explicit types when defining variables.

    # In Python, you can print using the 'print()' function, and you can use formatted strings
    # to easily insert variables into the string. This is similar to Java's 'System.out.println()' but more concise.
    # Java uses concatenation + or 'printf' for formatted output.

    # In Java:
    # System.out.println("Name: " + name);
    # System.out.printf("Age: %d\n", age);  // For formatted output in Java

    # In Python, formatted string (f-string) is more convenient:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} feet")
    print(f"Is student: {is_student}")


# In Python, indentation defines code blocks (functions, loops, etc.).
# In Java, code blocks are defined by curly braces {}, while Python relies on consistent indentation.
# The 'if __name__ == "__main__":' check ensures that the following block is only executed when this script
# is run directly, not when it's imported as a module in another script.
# In Java, this would be equivalent to having a 'main' method, which serves as the entry point for execution.

# In Java:
# public static void main(String[] args) {
#     displayVariables();  // Java calls a method inside main like this
# }

# This block runs the 'display_variables()' function if the script is run directly (not imported).
if __name__ == "__main__":
    # Calls the 'display_variables()' function when this script is executed.
    display_variables()
