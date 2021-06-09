# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
t = 0
l = 0

# Concatenate the string:
both_names = name1 + name2

# Lower case the string and remove white spaces:
both_names = (both_names.replace(" ", "")).lower()

# Initialise names list:
names = []
# Initialise true love lists:
true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]

# Append the letters of the string to the names list:
for letters in both_names:
  names.append(letters)
print(names)

print(both_names)
print(type(both_names))

# Concatenate the string:
# Lower case the string:
# Append the letters of the string to a list:
# Create lists for true and love:
# Compare the lists:
# Increase the counter for each true and love list.
# Concatenate the numbers:
# Compare the concatenated number to a an if statement:
# Print a score: