# Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show menu of operations
print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your choice (1-5): "))

# Perform calculation
if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
elif choice == 5:
    print("Result:", num1 % num2)
else:
    print("Invalid choice")
