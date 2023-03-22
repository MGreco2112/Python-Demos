# utilize looping structure to create squares (two lines at 90 degree angle, using turtle window as other two lines)

import turtle

DRAW_SPEED = 8
SQUARE_GAP = 10
INITIAL_LENGTH = 10
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0
x = 700
y = -650

turtle.penup()
turtle.goto(x, y)

turtle.pendown()
turtle.setheading(NORTH)
turtle.forward(INITIAL_LENGTH)
turtle.setheading(0)
turtle.forward(INITIAL_LENGTH)


turtle.done()