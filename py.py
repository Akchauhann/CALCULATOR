# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# Main program
def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Input from the user
    operation = input("Enter your choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation
    result = calculate(num1, num2, operation)

    # Display result
    print(f"The result is: {result}")

# Run the program
if __name__ == "__main__":
    main()
