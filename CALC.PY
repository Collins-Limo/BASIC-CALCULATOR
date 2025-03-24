
def calculator():
    print("Welcome to the simple calculator!")
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (addition, subtraction, multiplication, division): ").lower()

    # Perform the chosen operation
    if operation == "addition":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == "subtraction":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == "multiplication":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == "division":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")

