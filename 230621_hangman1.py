import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# ToDo1:
chosen_word = word_list[random.randint(0,len(word_list)-1)]
#or
# chosen_word = random.choice(word_list)

# ToDo2:
guess = input("Guess a letter: ").lower()

# ToDo3:
letter_used = 0

for letter in chosen_word:
  if letter == guess:
    letter_used += 1

if letter_used == 0:
  print("Letter guessed doesn't match any letters in the word.")
else:
  print(f"Letter guessed is used {letter_used} times in the word.")