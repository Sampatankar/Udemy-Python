from replit import clear
#HINT: You can call clear() to clear the output in the console.
"""
Put in a clear screen function when in IDE
"""

from art import logo

print(logo)

bidding = True
bidders = {}

while bidding:
  name = input("What is your name? ")
  bid = int(input("How much is your bid: £"))
  
  bidders[name] = bid

  others = input("Are there are others who wish to bid, yes or no? ")

  if others == "Yes" or others == "yes":
    clear()
    print(bidders)
  else:
    bidding = False
    clear()
    

print(bidders)
print("that's it folks!")

# Sort through list of values and display winner:
winners = []
for k,v in bidders.items():
  winners.append(v)

print(winners)
winners.sort(reverse=True)
print(winners)
# Then match the winning value in index[0] with winning key?
# More efficient way of handling this?