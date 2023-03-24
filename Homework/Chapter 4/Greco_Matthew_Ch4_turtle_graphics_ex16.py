# utilize looping structure to create squares (two lines at 90 degree angle, using turtle window as other two lines)

#import turtle
import turtle

SQUARE_COUNT = 150 #define var for number of loops iterated
DRAW_SPEED = 0 #draw speed variable
SQUARE_GAP = 5 #distance modifier for turtle's x coordinate
length = 5 #initial length of square sides
NORTH = 90 # heading for North
EAST = 0 # heading for East
x_cor = 370 #initial x coordinate starting location
Y_COR = -315 #initial y coordinate starting location

#set draw speed for fast drawing
turtle.speed(DRAW_SPEED)

#initialize for loop over range of square count
for squ in range(SQUARE_COUNT):
    turtle.penup() #lift pen
    turtle.goto(x_cor, Y_COR) #set turtle to location of x and y
    turtle.pendown() #drop pen
    turtle.setheading(NORTH) #set heading north
    turtle.forward(length) #draw line current length of square
    turtle.setheading(EAST) #set heading east
    turtle.forward(length) #draw line again
    x_cor -= SQUARE_GAP #modify x coordinate variable by square gap
    length += SQUARE_GAP #modify length variable by square gap



turtle.done() #display window post code execution