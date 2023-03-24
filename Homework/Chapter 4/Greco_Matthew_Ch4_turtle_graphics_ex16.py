# utilize looping structure to create squares (two lines at 90 degree angle, using turtle window as other two lines)

import turtle

SQUARE_COUNT = 150
DRAW_SPEED = 0
SQUARE_GAP = 5
length = 5
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0
x_cor = 370
Y_COR = -315

turtle.speed(DRAW_SPEED)

for x in range(SQUARE_COUNT):
    turtle.penup()
    turtle.goto(x_cor, Y_COR)
    turtle.pendown()
    turtle.setheading(NORTH)
    turtle.forward(length)
    turtle.setheading(0)
    turtle.forward(length)
    x_cor -= SQUARE_GAP
    length += SQUARE_GAP



turtle.done()