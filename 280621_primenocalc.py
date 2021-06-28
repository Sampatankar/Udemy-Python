#Write your code below this line 👇
def prime_checker(number):
  if number == 1 or number == 2 or (number % 1 == 0 and number % number == 0 and number % 2 != 0 and number % 3 != 0):
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# #Alternative solution:
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")

# Ultimately checks through every number between 2 and the number you input to see if it's divisible by any of them.

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)