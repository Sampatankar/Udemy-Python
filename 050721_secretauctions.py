from replit import clear
# This is a repl.it module...build your own 'os' module related clear screen func if needed!
# Google it!
#HINT: You can call clear() to clear the output in the console.
"""
Put in a clear screen function when in IDE
"""
# Import the art logo & print it:
from art import logo
print(logo)

# Initialise state and dictionary of bidders:
bidding = True
bidders = {}

# Begin bidding process:
while bidding:
  name = input("What is your name? ")
  bid = int(input("How much is your bid: $"))
  
  bidders[name] = bid

  others = input("Are there are others who wish to bid, yes or no? ")

  if others == "Yes" or others == "yes":
    clear()
  else:
    bidding = False
    clear()

# Create, sort and find winner:    
winner = []
for w in sorted(bidders, key=bidders.get, reverse=True):
  winner.append({w: bidders[w]})

# Clear screen and present winner details:
clear
for key, value in winner[0].items() :
    print(f"The winner is {key} with a bid of ${value}.")