#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

wanted_chars = []
l = 0
s = 0
n = 0

while l < nr_letters:
  wanted_chars.append(letters[random.randint(0,51)])
  l += 1

while s < nr_symbols:
  wanted_chars.append(symbols[random.randint(0,8)])
  s += 1

while n < nr_numbers:
  wanted_chars.append(numbers[random.randint(0,9)])
  n += 1

# print(wanted_chars)
random.shuffle(wanted_chars)
# print(wanted_chars)
print(f"Your new password is: {''.join(wanted_chars)}")

"""
Could have used:
for char in range(1, nr_letters+1):
  instead of while loop...etc
  + 1 as in range don't include the last number, we do want the actual number in nr_number, for example.
  No need to initialise l, s, and n and then to += 1 to them.
  No need to move from list, and can add characters directly to an initialised string.
  i.e. wanted_chars would be a string.
"""