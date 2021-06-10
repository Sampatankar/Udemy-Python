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

true = 'true'
love = 'love'

for t in true:
  print(both_names.count(t))
  print(type(both_names.count(t))) #  passes an integer

# # Initialise names list:
# names = []

# # Initialise true love lists:
# true = ["t", "r", "u", "e"]
# love = ["l", "o", "v", "e"]

# # Append the letters of the string to the names list:
# for letters in both_names:
#   names.append(letters)
# print(names)
# # Compare lists:
# true_value = set(names).intersection(true)
# love_value = set(names).intersection(love)

# print(true_value)
# print(len(true_value))
# print(love_value)
# print(len(love_value))

# # Derive the figures for calculation:
# both_figures = str(len(true_value)) +str(len(love_value))
# both_figures = both_figures.replace(" ", "")
# both_figures = int(both_figures)

# # Love 'calculation' through if/else statements:
# if both_figures <10 or both_figures > 90:
#   print(f"Your score is {both_figures}, you go together like coke and mentos.")
# elif both_figures > 40 and both_figures < 50:
#   print(f"Your score is {both_figures}, you are alright together.")
# else:
#   print(f"Your score is {both_figures}.")