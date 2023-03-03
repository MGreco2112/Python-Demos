#create hit the target demonstration without referencing the code

#turtle moves in x,y in goto statements
#x is horizontal, y is vertial axies

def takeSpeedInput():
    output = turtle.numinput("Speed Input", "Enter the speed you wish to fire at (1 - 10): ")

    return output

#import turtle graphics package
import turtle

#set constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_ANGLE = 90
TARGET_SIDES = 4
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
DEFAULT_SPEED_VALUE = 0
MAXIMUM_SPEED_VALUE = 10

#angle 68
#force 9

#setup window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#background color
turtle.bgcolor("blue")
#set pen color to red
turtle.pencolor("red")

#hide turtle
turtle.hideturtle()
#set draw speed to 0
turtle.speed(0)
#lift pen
turtle.penup()
#move turtle to lower left corner of target
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
#drop pen
turtle.pendown()
#enter loop to draw square
for sides in range(TARGET_SIDES):
    turtle.forward(TARGET_WIDTH)
    turtle.left(TARGET_ANGLE)
#lift pen
turtle.penup()
#return to origin
turtle.goto(0,0)
#set turtle pointing east
turtle.setheading(0)
#drop pen
turtle.pendown()
#increase turtle speed to 1
turtle.speed(1)
#show turtle
turtle.showturtle()
#set speed to projectile speed
turtle.speed(PROJECTILE_SPEED)

#take user inputs
angle = turtle.numinput("Angle", "Enter the angle you wish to fire the projectile at: ")
speed = DEFAULT_SPEED_VALUE

#error correct for invalid inputs on speed variable
while speed <= DEFAULT_SPEED_VALUE or speed > MAXIMUM_SPEED_VALUE:
    speed = takeSpeedInput()

#initialize force variable with speed * FORCE_FACTOR
force = speed * FORCE_FACTOR

#set heading from angle input
turtle.setheading(angle)

#move turtle forward by calculated force
turtle.forward(force)

#determine hit
if turtle.xcor() >= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and turtle.ycor() >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH):
    turtle.write("HIT!")
    print(f"X POS: {turtle.xcor():.2f}, Y POS: {turtle.ycor():.2f}")
else:
    turtle.write("MISS!")
    turtle_x_difference = turtle.xcor() - TARGET_LLEFT_X
    turtle_y_difference = turtle.ycor() - TARGET_LLEFT_Y
    print(f"X Difference: {turtle_x_difference:,.2f}, Y DIFFERENCE: {turtle_y_difference:.2f}")

#keep window open after instructions finish
turtle.done()