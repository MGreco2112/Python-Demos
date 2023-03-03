#modify the Hit The Target game to give the user hints to as to better angle and force used for further attempts

#Hit The Target code

#import Turtle Graphics library
import turtle

#constants
SCREEN_WIDTH = 600 #window width at 600px
SCREEN_HEIGHT = 600 #window height at 600px
TARGET_LLEFT_X = 100 #lower left X coordinate of target
TARGET_LLEFT_Y = 250 #lower left y coordinate of target
TARGET_WIDTH = 25 #width of target in px
FORCE_FACTOR = 30 #force factor
TARGET_SIDES = 4 #number of sides of target
TARGET_ANGLE_DEGREES = 90 #the degree of the angles on each of the sides of target
PROJECTILE_SPEED = 1 #animation speed for turtle
NORTH = 90 #heading coordinate for North
SOUTH = 270 #heading coordinate for South
EAST = 0 #heading coordinate for East
WEST = 180 #heading coordinate for West

#create Window for Turtle at Width and Height specifications
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#draw target
turtle.hideturtle() #make turtle icon invisible
turtle.speed(0) #set turtle movement speed to 0
turtle.penup() #lift turtle pen
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y) #move turtle to lower left corner of to be drawn target
turtle.pendown() #drop pen
turtle.setheading(EAST) #point turtle towards heading 0
for line in range(TARGET_SIDES): #enter for loop running for number of sides of target
    turtle.forward(TARGET_WIDTH) #move turtle forward width of target
    turtle.left(TARGET_ANGLE_DEGREES) #rotate turtle 90 degrees to the left
turtle.penup() #lift pen

#center turtle
turtle.goto(0,0) #return turtle to 0px x 0px
turtle.setheading(EAST) #point turtle towards 0 heading
turtle.showturtle() #reveal turtle location on plane
turtle.speed(PROJECTILE_SPEED) #increase draw speed from 0 to 1

#take user input for angle and force
angle = float(turtle.numinput("Angle Input", "Enter the angle for firing the projectile")) #take numeric input from user to determine the angle of shot to be taken
force = float(turtle.numinput("Force Input", "Enter the launce force (1 - 10)")) #tale numeric input from user to determine the force given to the projectile

#calculate the distance projectile will travel
distance = force * FORCE_FACTOR

#set heading
turtle.setheading(angle) #user input passed into setheading method

#launch projectile
turtle.pendown() #drop pen
turtle.forward(distance) #move turtle forward calculated distance

#check for success

#if current turtle x coordinate larger or equal to target lower left x and less or equal to target lower left x + width of target and
#turtle y coordiante greater or equal to target lower left y and less or equal to lower left y plus target width
#then a hit is successfully registered
if turtle.xcor() >= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and turtle.ycor() >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH):
    turtle.write("Target hit!!!") #turtle writes Target hit
    turtle.penup() #lift pen
    turtle.goto(0,0) #return to position 0 x 0 px
else: #if hit not registered
    
    if turtle.xcor() < TARGET_LLEFT_X: #if turtle's x coordinate less than target's lower left x coordinate
        turtle.write("Try decreasing the angle.") #turtle writes the decrease angle hit
    elif turtle.ycor() >= TARGET_LLEFT_X: #if y coordinate is greater than target's lower left x
        turtle.write("Try increasing the angle.") #turtle writes increase angle hint
    
    if turtle.pos()[0] < (TARGET_LLEFT_X + TARGET_WIDTH) and turtle.pos()[1] < (TARGET_LLEFT_Y + TARGET_WIDTH): #if turtle's x coordinate is less than target hitbox
        turtle.penup() #lift pen
        turtle.goto(0,0) #return to position 0 x 0 px
        turtle.write("Try increasing the force.") #write increase force hint

    elif turtle.pos()[0] > (TARGET_LLEFT_X) or turtle.pos()[1] > (TARGET_LLEFT_Y): #if turtle's x coordinate greater than target's lower left axis or greater than target's lower right axis
        turtle.penup() #lift pen
        turtle.goto(0,0) #return to position 0 x 0 px
        turtle.write("Try decreasing the force.") #print increase force hint


turtle.done() #leave turtle window open once animation finishes