# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Convert numbers into two numbers and put them into a list:
position = list(position)

# Which row?
which_row = int(position[1])
# print(f"which row: {which_row}")

# Which column?
which_col = int(position[0])
# print(f"which column: {which_col}")

# Convert row and column numbers into position in nested lists:
map[which_row-1][which_col-1] = "X"



"""
Steps to build this out:
1. Convert numbers into two numbers (split?) - done
2. Last number chooses which object to go to (row1 etc)
3. First number chooses which column to go to (0, 1 or 2?)
4. remove emoji and replace with 'X'
"""




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")