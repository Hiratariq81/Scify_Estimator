import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

def scientific_calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")

    choice = input("Enter choice (1-11): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {power(num1, num2)}")

    elif choice == '6':
        num = float(input("Enter number: "))
        print(f"Result: {sqrt(num)}")

    elif choice == '7':
        num = float(input("Enter number: "))
        base = input("Enter base (default is e): ")
        if base:
            base = float(base)
            print(f"Result: {logarithm(num, base)}")
        else:
            print(f"Result: {logarithm(num)}")

    elif choice in ['8', '9', '10']:
        num = float(input("Enter angle in degrees: "))

        if choice == '8':
            print(f"Result: {sine(num)}")
        elif choice == '9':
            print(f"Result: {cosine(num)}")
        elif choice == '10':
            print(f"Result: {tangent(num)}")

    elif choice == '11':
        num = int(input("Enter number: "))
        print(f"Result: {factorial(num)}")

    else:
        print("Invalid Input")

# Run the calculator
scientific_calculator()
