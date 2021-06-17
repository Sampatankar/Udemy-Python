# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Code above creates a list of integers:
# Start counter for total height and no's of heights:
total = 0
no_heights = 0

# For loop to check through each 'height' in list and add to total
# , and increase no's of heights:
for height in student_heights:
  total += height
  no_heights += 1

# Calculate the average height then round to nearest whole integer:
average_height = round(total / no_heights)
print(average_height)