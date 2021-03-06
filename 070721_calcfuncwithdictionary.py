# Calculator:

# Add:
def add(n1, n2):
  return n1 + n2

# Subtract:
def subtract(n1, n2):
  return n1 - n2

# Multiply:
def multiply(n1, n2):
  return n1 * n2

# Divide:
def divide(n1, n2):
  return n1 / n2

# Dictionary:
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# Inputs:
num1 = int(input("What's the first number: "))

for k in operations:
  print(k)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number: "))

# Calculator:
if operation_symbol in operations.keys():
  answer = operations[operation_symbol](num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")