# GO TO:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()


"""
This code works because I had enunciated an algorithm that
simply follows hard along the right edge.
Once the right wall disappears, there was turn right and move.
Once the right wall re-appears, you move, until you hit the
the wall in front, then you turn left, and then the process loops.
The process loops until we reach the flag finish.

This process works for hurdles as we start from the left.
It also therefore works for the maze challenge:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""