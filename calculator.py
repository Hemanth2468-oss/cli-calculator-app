

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Banner
print("=" * 45)
print("         CLI CALCULATOR APP")
print("=" * 45)
print("|  1. ADDITION        (+)           |")
print("|  2. SUBTRACTION     (-)           |")
print("|  3. MULTIPLICATION  (*)           |")
print("|  4. DIVISION        (/)           |")
print("|  5. EXIT                          |")
print("=" * 45)


while True:

    choice = input("\nEnter your choice (1-5): ")

    if choice == '5':
        print("\nThank you for using Calculator!")
        break

    if choice in ['1', '2', '3', '4']:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result =", add(num1, num2))

        elif choice == '2':
            print("Result =", subtract(num1, num2))

        elif choice == '3':
            print("Result =", multiply(num1, num2))

        elif choice == '4':
            print("Result =", divide(num1, num2))

    else:
        print("Invalid choice! Please try again.")
