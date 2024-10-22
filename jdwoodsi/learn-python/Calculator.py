num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = float(num1)
num2 = float(num2)

operationType = input("Enter type of operation (+, -, *, /, ^ or %): ")

if operationType == "+":
    if (abs(num1 + num2) % 1) < 1 and abs(num1 + num2) % 1 > 0:
        print(num1 + num2)
    else:
        print(int(num1) + int(num2))
elif operationType == "-":
    if (abs(num1 + num2) % 1) < 1 and abs(num1 + num2) % 1 > 0:
        print(num1 - num2)
    else:
        print(int(num1) - int(num2))
elif operationType == "*":
    if (abs(num1 + num2) % 1) < 1 and abs(num1 + num2) % 1 > 0:
        print(num1 * num2)
    else:
        print(int(num1) * int(num2))
elif operationType == "/":
    if (abs(num1 + num2) % 1) < 1 and abs(num1 + num2) % 1 > 0:
        print(num1 / num2)
    else:
        print(int(num1) / int(num2))
elif operationType == "^":
    if (abs(num1 + num2) % 1) < 1 and abs(num1 + num2) % 1 > 0:
        print(pow(num1, num2))
    else:
        print(int(pow(num1, num2)))
elif operationType == "%":
    if (abs(num1 + num2) % 1) < 1 and abs(num1 + num2) % 1 > 0:
        print(num1%num2)
    else:
        print(int(num1%num2))
else:
    print("Invalid input, please try again")

