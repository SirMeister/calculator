class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

# User interaction
calc = Calculator()
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply): ")

if operation == 'add':
    print(f"The result is: {calc.add(a, b)}")
elif operation == 'subtract':
    print(f"The result is: {calc.subtract(a, b)}")
elif operation == 'multiply':
    print(f"The result is: {calc.multiply(a, b)}")
else:
    print("Invalid operation!")