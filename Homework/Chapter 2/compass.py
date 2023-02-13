#import Turtle module
import turtle
#import Time module for waiting
import time

#Compass Drawing
#set background color to blue
turtle.bgcolor("gray")
#lift pen
turtle.penup()
#move turtle to position 0 x 400 px
turtle.goto(0, 200)
#position turtle facing South
turtle.setheading(270)
#drop pen
turtle.pendown()
#move turtle South 400px
turtle.forward(400)
#lift pen
turtle.penup()
#move turtle to -200 x 0 px
turtle.goto(-200, 0)
#drop pen
turtle.pendown()
#position turtle facing East
turtle.setheading(0)
#move turtle forward 400 px
turtle.forward(400)
#lift pen
turtle.penup()
#move turtle to -25 x 25 px
turtle.goto(-20, 20)
#position turtle facing
turtle.setheading(222)
#drop pen
turtle.pendown()
#draw 50 px diameter circle
turtle.circle(30)
#lift pen
turtle.penup()
#postion turtle North of tip of North line
turtle.goto(-15, 210)
#write North
turtle.write("NORTH")
#move turtle to -15 x -220
turtle.goto(-15, -220)
#write SOUTH
turtle.write("SOUTH")
#position turtle at -240 x -7
turtle.goto(-240, -7)
#write West
turtle.write("WEST")
#position turtle at 7 x 240
turtle.goto(210, -7)
#write East
turtle.write("EAST")
#move position to 0 x 0
turtle.goto(0,0)

#wait before moving to next drawing
time.sleep(3)

#clear drawing, pen and fill settings, and reset turtle location, but not background color
turtle.reset()

#Adjacent Diamonds
#lift pen
turtle.penup()
#position turtle at 100 x 100 px
turtle.goto(-100, 100)
#lower pen
turtle.pendown()
#set fill color
turtle.fillcolor("white")
#activate filling
turtle.begin_fill()
#turn turtle right by 130
turtle.right(135)
#move turtle forward by 100
turtle.forward(100)
#turn turtle left by 90
turtle.left(90)
#move turtle forward 100
turtle.forward(100)
#turn turtle left by 90
turtle.left(90)
#move turtle forward by 100
turtle.forward(100)
#store location in variable
turtlePosition = turtle.pos()
#turn turtle left by 90
turtle.left(90)
#move turtle forward 100
turtle.forward(100)
#end filling
turtle.end_fill()
#position turtle at location saved in turtlePosition
turtle.goto(turtlePosition[0], turtlePosition[1])
#turn turtle right by 90
turtle.right(90)
#begin fill
turtle.begin_fill()
#loop to repeat steps
for x in range(4):
    #move turtle forward 100
    turtle.forward(100)
    #turn turtle right 90
    turtle.right(90)
#fill in shape
turtle.end_fill()

#wait three seconds before drawing next piece
time.sleep(3)

#clear screen and reset turtle position, keeps background color
turtle.reset()

#keep window open after reaching last line
turtle.done()