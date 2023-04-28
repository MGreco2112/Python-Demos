#Greco_Matthew_Ex2_Prob5

#Snowman Turtle Graphics

#Create the snowman graphic as illustrated in the assignment page
#Utilize the following function names withing the program:
    #draw_base
    #draw_mid_section
    #draw_arms
    #draw_head
    #draw_pipe
    #draw_hat
    #draw_buttons

#---BEGIN PROGRAM---

#import turtle graphics module
import turtle

#define constants for compass directions
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0

#initialize constants for the radiases of three circles
CIRCLE_RAD_A = 75
CIRCLE_RAD_B = 50
CIRCLE_RAD_C = 30

#set constants for pipe square length, angle, and side count
PIPE_SIDES = 4
PIPE_ANGLE = 90
PIPE_LENGTH = 10
    
#define main function
def main():
    #initialize button count constant to 4
    BUTTON_COUNT = 4

    #call draw base function
    draw_base()
    #call draw mid section function
    draw_mid_section()
    #call draw arms function
    draw_arms()
    #call draw head function
    draw_head()
    #call draw hat function
    draw_hat()

    #define for loop in range of 0, 3 for number of buttons
    for button in range(BUTTON_COUNT):
        #call draw button function
        draw_button()
    
    #call turtle done function to keep turtle window open
    turtle.done()

#define draw base function
def draw_base():
    #lift pen
    turtle.penup()
    #set heading north
    turtle.setheading(NORTH)
    #move turtle forward 50px
    turtle.forward(50)
    #set heading west
    turtle.setheading(WEST)
    #drop pen
    turtle.pendown()
    #draw circle of rad 75
    turtle.circle(CIRCLE_RAD_A)

def draw_mid_section():
    #lift pen
    turtle.penup()
    #set heading east
    turtle.setheading(EAST)
    #drop pen
    turtle.pendown()
    #draw circle of rad
    turtle.circle(CIRCLE_RAD_B)

def draw_arms():
    #Draw Left Arm

    #lift pen
    turtle.penup()
    #set heading north
    turtle.setheading(NORTH)
    #move turtle forward radias of circle
    turtle.forward(CIRCLE_RAD_B)
    #store radius of circle b in two variables for later reference
    radius_b_x = turtle.xcor()
    radius_b_y = turtle.ycor()
    #set heading west
    turtle.setheading(WEST)
    #move turtle to east edge of the mid section
    turtle.forward(CIRCLE_RAD_B)
    #turn turtle to the right
    turtle.right(CIRCLE_RAD_B / 2)
    #drop pen
    turtle.pendown()
    #move turtle forward
    turtle.forward(CIRCLE_RAD_B)
    #turn turtle right
    turtle.right(45)
    #move turtle forward
    turtle.forward(CIRCLE_RAD_B)
    #lift pen
    turtle.penup()
    #turn turtle left
    turtle.right(175)
    #move turtle forward
    turtle.forward(10)
    #move turtle right
    turtle.right(90)
    #drop pen
    turtle.pendown()
    #move turtle forward
    turtle.forward(10)
    #lift pen
    turtle.penup()
    #move turtle to radius of circle b
    turtle.goto(radius_b_x, radius_b_y)

    #Draw Right Arm

    #set heading east
    turtle.setheading(EAST)
    #move turtle to east edge of circle
    turtle.forward(CIRCLE_RAD_B)
    #move turtle left
    turtle.left(50)
    #drop pen
    turtle.pendown()
    #move turtle forward
    turtle.forward(50)
    #move turtle left
    turtle.left(25)
    #move turtle forward
    turtle.forward(10)
    #lift pen
    turtle.penup()
    #move turtle left
    turtle.left(177)
    #move turtle forward
    turtle.forward(10)
    #turn turtle left
    turtle.left(80)
    #drop pen
    turtle.pendown()
    #move turtle forward
    turtle.forward(10)
    #lift pen
    turtle.penup()
    #move turtle to center of circle b
    turtle.goto(radius_b_x, radius_b_y)
    #set heading north
    turtle.setheading(NORTH)
    #move turtle forward radius of circle B so turtle is at the top edge of the circle
    turtle.forward(CIRCLE_RAD_B)


def draw_head():
    #draw head circle

    #set heading east
    turtle.setheading(EAST)
    #drop pen
    turtle.pendown()
    #draw circle of radius set by constant for circle c
    turtle.circle(CIRCLE_RAD_C)

    #create variables for start of circle coordinates
    radius_c_x = turtle.xcor()
    radius_c_y = turtle.ycor()

    #draw facial features
    #mouth

    #lift pen
    turtle.penup()
    #set heading north
    turtle.setheading(NORTH)
    #move turtle forward
    turtle.forward(20)
    #set heading west
    turtle.setheading(WEST)
    #drop pen
    turtle.pendown()
    #move turtle forward
    turtle.forward(20)
    #set heading east
    turtle.setheading(EAST)
    #move turtle forward
    turtle.forward(40)
    #lift pen
    turtle.penup()
    #set heading west
    turtle.setheading(WEST)
    #move turtle forward
    turtle.forward(10)

    #function call to draw pipe
    draw_pipe()

    #eyes

    #move turtle to start location of circle c
    turtle.goto(radius_c_x, radius_c_y)
    #set heading north
    turtle.setheading(NORTH)
    #move turtle forward radius of circle c
    turtle.forward(CIRCLE_RAD_C)
    #set heading east for right eye
    turtle.setheading(EAST)
    #move turtle forward
    turtle.forward(10)
    #drop pen
    turtle.pendown()
    #draw circle of rad 5
    turtle.circle(5)
    #lift pen
    turtle.penup()
    #set heading west
    turtle.setheading(WEST)
    #move turtle forward
    turtle.forward(20)
    #set heading east
    turtle.setheading(EAST)
    #drop pen
    turtle.pendown()
    #draw circle for left eye
    turtle.circle(5)
    #lift pen
    turtle.penup()

    #position for hat
    turtle.goto(radius_c_x, radius_c_y)
    #set heading north
    turtle.setheading(NORTH)
    #initialize var for distance between bottom of circle c and bottom rim of to-be-drawn hat
    hat_start_distance = (CIRCLE_RAD_C * 2) - 10
    #move turtle forward circumference of circle c - 10 for lower border of hat
    turtle.forward(hat_start_distance)




    
def draw_pipe():
    #set heading east
    turtle.setheading(EAST)
    #turn turtle right
    turtle.right(25)
    #drop pen
    turtle.pendown()
    #move turtle forward
    turtle.forward(40)
    #set color and fill color to blue
    turtle.color("blue")
    turtle.fillcolor("blue")
    #begin fill
    turtle.begin_fill()
    #define loop to draw square
    for side in range(PIPE_SIDES):
        turtle.left(PIPE_ANGLE)
        turtle.forward(PIPE_LENGTH)
    #end fill
    turtle.end_fill()
    #lift pen
    turtle.penup()
    #set colors back to black
    turtle.color("black")
    turtle.fillcolor("black")
    


def draw_hat():
    pass
def draw_button():
    pass

#call main function
main()

