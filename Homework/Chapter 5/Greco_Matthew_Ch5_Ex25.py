#create a checkerboard with alternating white and black squares covering the canvas

#import turtle module
import turtle

#define square width global constant
SQUARE_WIDTH = 20
#define square angle constant
SQUARE_ANGLE = 90
#define square sides constant
SQUARE_SIDES = 4
#define heading direction constants
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

#define global vars for x_coor and y_coor
x_coor = -60
y_coor = 0

#define constants for starting x and y coors
STARTING_X = -60
STARTING_Y = 0

#define main function
def main():
    #create pointers to global vars x_coor and y_coor
    global x_coor
    global y_coor

    #iterate from 1 to 3
    for board_stage in range(1, 4):

        #if second iteration of board_stage
        if board_stage == 2:
            #lift pen
            turtle.penup()
            #reset x_coor to STARTING_X
            x_coor = STARTING_X
            #reset y_coor to STARTING_Y + (SQUARE_WIDTH * 2)
            y_coor = STARTING_Y + (SQUARE_WIDTH * board_stage)
        #else if third iteration of board_stage
        elif board_stage == 3:
            #lift pen
            turtle.penup()
            #reset x_coor to STARTING_X
            x_coor = STARTING_X
            #set y_coor to STARTING_Y + (20 + 60)
            y_coor = STARTING_Y + (SQUARE_WIDTH + 60)

        #iterate from 0 to 1
        for row in range(2):
            #call black square function with x_coor and y_coor
            black_square(x_coor, y_coor)
            #add the width of the square (20) to current x_coor
            x_coor += SQUARE_WIDTH
            #call white square function with updated x_coor and y_coor
            white_square(x_coor, y_coor)
            #increment x_coor by width of square
            x_coor += SQUARE_WIDTH
        #call black square function to account for odd number of checker board squares per row
        black_square(x_coor, y_coor)

        #if board stage is not on final iteration
        if board_stage != 3:
            #lift pen
            turtle.penup()
            #set x_coor to starting x
            x_coor = STARTING_X
            #if board stage is not on second iteration
            if board_stage != 2:
                #y coor is set to starting y plus square width
                y_coor = STARTING_Y + SQUARE_WIDTH
            else: #otherwise, if second iteration
                #y coor is set to starting y plus 60
                y_coor = STARTING_Y + 60
            
            #iterate from 0 to 1
            for row in range(2):
                #call white square function on x_coor and y_coor
                white_square(x_coor, y_coor)
                #increment x_coor by square_width
                x_coor += SQUARE_WIDTH
                #call black square function with update x_coor and y_coor
                black_square(x_coor, y_coor)
                #increment x_coor by square width
                x_coor += SQUARE_WIDTH
            #call white square function to account for odd number of squares per checkerboard row
            white_square(x_coor, y_coor)


    #keep turtle window open
    turtle.done()

#define white square function with x and y coors
def white_square(x, y):
    #lift pen
    turtle.penup()
    #goto x, y
    turtle.goto(x, y)
    #set fill color to white
    turtle.fillcolor("white")
    #drop pen
    turtle.pendown()
    #begin filling shape
    turtle.begin_fill()
    #loop from 0 to three, based on range function return of SQUARE_SIDES
    for count in range(SQUARE_SIDES):
        #move turtle forward the width of the square
        turtle.forward(SQUARE_WIDTH)
        #turn turtle left 90
        turtle.left(SQUARE_ANGLE)
    #fill shape with color
    turtle.end_fill()


#define black square function
def black_square(x, y):
        #lift pen
    turtle.penup()
    #goto x, y
    turtle.goto(x, y)
    #set fill color to white
    turtle.fillcolor("black")
    #drop pen
    turtle.pendown()
    #begin filling shape
    turtle.begin_fill()
    #loop from 0 to three, based on range function return of SQUARE_SIDES
    for count in range(SQUARE_SIDES):
        #move turtle forward the width of the square
        turtle.forward(SQUARE_WIDTH)
        #turn turtle left 90
        turtle.left(SQUARE_ANGLE)
    #fill shape with color
    turtle.end_fill()


#call main function
main()