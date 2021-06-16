import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

# Your choice:
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if choice < 0 or choice > 2:
  print("You made an invalid choice!")
else:
  if choice == 0:
    print(moves[0])
  elif choice == 1:
    print(moves[1])
  elif choice == 2:
    print(moves[2])

  # Random comp choice:
  comp_choice = random.randint(0,2)
  if comp_choice == 0:
    print(moves[0])
  elif comp_choice == 1:
    print(moves[1])
  elif comp_choice == 2:
    print(moves[2])

  # Outcome of game:
  if choice == comp_choice:
    print("Draw!")
  elif (choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1):
    print("You Win!")
  else:
    print("You Lose!")