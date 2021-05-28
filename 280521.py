# Odd or Even number checker:
number = int(input("Which number do you want to check? "))

if number % 2 != 0:
  print("This is an odd number.")
else:
  print("This is an even number.")


  # Enhanced BMI Calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
b = round(bmi, 1)

if b < 18.5:
  print(f"Your BMI is {b}, you are underweight.")
elif b < 25:
  print(f"Your BMI is {b}, you are normal weight.")
elif b < 30:
  print(f"Your BMI is {b}, you are slightly overweight.")
elif b < 35:
  print(f"Your BMI is {b}, you are obese.")
else:
  print(f"Your BMI is {b}, you are clinically obese.")