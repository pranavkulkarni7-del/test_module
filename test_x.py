# Assign values to num1 and num2
num1 = 10
num2 = 5

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division with safety check
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Display results
print("Results:")
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)
