# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Concatenate the string:
both_names = name1 + name2

# Lower case the string and remove white spaces:
both_names = (both_names.replace(" ", "")).lower()

# Initialise the strings to check against and counters for value:
true = 'true'
love = 'love'

t_value = 0
l_value = 0

# Loops to check through names:
for t in true:
  t_value += both_names.count(t)

for l in love:
  l_value += both_names.count(l)

# Concatenate the two numbers and make int:
both_figures = int(str(t_value) + str(l_value))

# Love 'calculation' through if/else statements:
if both_figures <10 or both_figures > 90:
  print(f"Your score is {both_figures}, you go together like coke and mentos.")
elif both_figures > 40 and both_figures < 50:
  print(f"Your score is {both_figures}, you are alright together.")
else:
  print(f"Your score is {both_figures}.")