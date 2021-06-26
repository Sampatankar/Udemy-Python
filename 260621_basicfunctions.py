# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
  print("First print statement.")
  print("Second print statement.")
  print("Third print statement.")

greet()


# Multiple params:
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# Using positional arguments:
greet_with("Sameer", "Bradford")
  

# Using keyword arguments:
greet_with(name="Sameer", location="Grenada")