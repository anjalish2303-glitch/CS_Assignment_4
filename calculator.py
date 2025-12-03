print("=== Python Calculator ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print("Enter choice (1/2/3/4):")
choice = input()
print("Enter first number:")
num1 = float(input()) 
print("Enter second number:")
num2 = float(input())

result = 0.0

if choice == '1':
    # Operation 1: Addition
    result = num1 + num2
elif choice == '2':
    # Operation 2: Subtraction
    result = num1 - num2
elif choice == '3':
    # Operation 3: Multiplication
    result = num1 * num2
elif choice == '4':
    # Operation 4: Division
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
        exit()
else:
    print("Invalid choice.")
    exit()

print(f"Result: {result}")