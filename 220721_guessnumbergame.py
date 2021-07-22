import random

print("GUESS THE NUMBER\n")

print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  attempts = 10
elif difficulty == 'hard':
  attempts = 5


while attempts > 0:
  if attempts > 1:
    chosen_number = int(input("Make a guess: "))
    if chosen_number > number:
      print("Too high.\nGuess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif chosen_number < number:
      print("Too low.\nGuess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif chosen_number == number:
      print(f"You got it! The answer was {number}.")
  elif attempts > 0:
    chosen_number = int(input("Make a guess: "))
    if chosen_number > number or chosen_number < number:
      print("You've run out of guesses, you lose.")
      attempts -= 1
    elif chosen_number == number:
      print(f"You got it! The answer was {number}.")