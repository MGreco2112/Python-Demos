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
    #call draw pipe function
    draw_pipe()
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
    turtle.circle(75)

def draw_mid_section():
    pass
def draw_arms():
    pass
def draw_head():
    pass
def draw_pipe():
    pass
def draw_hat():
    pass
def draw_button():
    pass

#call main function
main()

