#import Turtle module
import turtle
#import Time module for waiting
import time

#set background color to gray
turtle.bgcolor("gray")

#Compass Drawing

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
time.sleep(2)

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

#wait two seconds before drawing next piece
time.sleep(2)

#clear screen and reset turtle position, keeps background color
turtle.reset()

#Olympic Rings

#lift pen
turtle.penup()
#move Turtle to -200 x 50 px
turtle.goto(-200, 50)
for x in range(3):
    #drop pen
    turtle.pendown()
    #draw circle of dia 50px
    turtle.circle(50)
    #lift pen
    turtle.penup()
    #move turtle forward 150px
    turtle.forward(150)
#turn turtle facing West
turtle.setheading(180)
#save current location in turtlePosition variable
turtlePosition = turtle.pos()
#increase x axis position by 50px
turtle.goto(turtlePosition[0], turtlePosition[1] + 50)
#move turtle 225 px, between two rings
turtle.forward(225)
for x in range(2):
    #drop pen
    turtle.pendown()
    #draw circle
    turtle.circle(50)
    #lift pen
    turtle.penup()
    #move forward 225px
    turtle.forward(150)

#wait before moving to next drawing
time.sleep(2)

#clear drawing, pen and fill settings, and reset turtle location, but not background color
turtle.reset()

#Double Triangle

#lift pen
turtle.penup()
#move turtle to position 0 x 200
turtle.goto(0, 200)
#drop pen
turtle.pendown()
#move turtle to position -100 x 0
turtle.goto(-100, 0)
#move turtle to position  100 x 0
turtle.goto(100, 0)
#move turtle to position 0 x 200
turtle.goto(0, 200)
#lift pen
turtle.penup()
#move turtle to position 0 x 100
turtle.goto(0,100)
#change fill color to white
turtle.fillcolor("white")
#pen down
turtle.pendown()
#start fill
turtle.begin_fill()
#move to position -100 x 0
turtle.goto(-100, 0)
#move turtle to positioon 100 x 0
turtle.goto(100, 0)
#move turtle to position 0 x 100
turtle.goto(0, 100)
#end fill
turtle.end_fill()

#wait before moving to next drawing
time.sleep(2)

#clear drawing, pen and fill settings, and reset turtle location, but not background color
turtle.reset()

#square with dashes and points

#lift pen
turtle.penup()
#move turtle to position 200 x 200
turtle.goto(200, 200)
#pen down
turtle.pendown()
#make dot
turtle.dot()
#move turtle to 0 x 0
turtle.goto(0, 0)
#make dot
turtle.dot()
#move turtle to position -200 x -200
turtle.goto(-200, -200)
#make dot
turtle.dot()
#move turtle to -200 x 200
turtle.goto(-200, 200)
#make dot
turtle.dot()
#move turlte to 200 x -200
turtle.goto(200, -200)
#make dot
turtle.dot()
#set heading to 180
turtle.setheading(180)
#move turtle forward by 25px
turtle.forward(25)
#lift pen
turtle.penup()
#move turtle forward by 50px
turtle.forward(75)
#drop pen
turtle.pendown()
#move turtle ahead 50px
turtle.forward(75)
#lift pen
turtle.penup()
#move tutle forward 50px
turtle.forward(75)
#drop pen
turtle.pendown()
#move turtle ahead 50px
turtle.forward(75)
#lift pen
turtle.penup()
#move tutle forward 50px
turtle.forward(45)
#drop pen
turtle.pendown()
#move turtle to -200 x -200
turtle.goto(-200, -200)
#lift pen
turtle.penup()
#move turtle to -200 x 200
turtle.goto(-200, 200)
#set heading East
turtle.setheading(0)
#drop pen
turtle.pendown()
#move turtle forward by 25px
turtle.forward(25)
#lift pen
turtle.penup()
#move turtle forward by 50px
turtle.forward(75)
#drop pen
turtle.pendown()
#move turtle ahead 50px
turtle.forward(75)
#lift pen
turtle.penup()
#move tutle forward 50px
turtle.forward(75)
#drop pen
turtle.pendown()
#move turtle ahead 50px
turtle.forward(75)
#lift pen
turtle.penup()
#move tutle forward 50px
turtle.forward(45)
#drop pen
turtle.pendown()
#move turtle to 200 x 200
turtle.goto(200, 200)
#move turtle to 200 x -200
turtle.goto(200, -200)

#wait before moving to next drawing
time.sleep(2)

#clear drawing, pen and fill settings, and reset turtle location, but not background color
turtle.reset()

#three dimensional rectangle

#first square coordinate variables
firstUpperLeft = 0
firstUpperRight = 0
firstBottomLeft = 0
firstBottomRight = 0

#secord square coordinate variables
secondUpperLeft = 0
secondUpperRight = 0
secondBottomLeft = 0
secondBottomRight = 0

#lift pen
turtle.penup()
#move turtle to 0 x 200
turtle.goto(100, 0)
#set firstUpperLeft to position
firstUpperLeft = turtle.pos()
#drop pen
turtle.pendown()
#set heading East
turtle.setheading(0)
#move turtle forward 100px
turtle.forward(100)
#set firstUpperRight to position
firstUpperRight = turtle.pos()
#set heading to South
turtle.setheading(270)
#move turtle 100px forward
turtle.forward(100)
#set firstBottomRight to position
firstBottomRight = turtle.pos()
#set heading West
turtle.setheading(180)
#move forward 100px
turtle.forward(100)
#set firstBottomLeft to position
firstBottomLeft = turtle.pos()
#move turtle to 0 x 200
turtle.goto(100, 0)
#set secondBottomRight to position
secondBottomRight = turtle.pos()
#set heading north
turtle.setheading(90)
#move turtle forward 100px
turtle.forward(100)
#set secondUpperRight to position
secondUpperRight = turtle.pos()
#set heading West
turtle.setheading(180)
#move turtle forward 100px
turtle.forward(100)
#set secondUpperLeft to position
secondUpperLeft = turtle.pos()
#set heading south
turtle.setheading(270)
#move turtle forward 100px
turtle.forward(100)
#set secondBottomLeft to position
secondBottomLeft = turtle.pos()
#set heading East
turtle.setheading(0)
#move turtle forward 100px
turtle.forward(100)
#lift pen
turtle.penup()
#move turtle to firstBottomLeft
turtle.goto(firstBottomLeft)
#drop pen
turtle.pendown()
#move turtle to secondBottomLeft
turtle.goto(secondBottomLeft)
#lift pen
turtle.penup()
#move turtle to secondUpperLeft
turtle.goto(secondUpperLeft)
#drop pen
turtle.pendown()
#move turtle to firstUpperLeft
turtle.goto(firstUpperLeft)
#lift pen
turtle.penup()
#move turtle to firstUpperRight
turtle.goto(firstUpperRight)
#drop pen
turtle.pendown()
#move turtle to secondUpperRight
turtle.goto(secondUpperRight)
#lift pen
turtle.penup()
#move turtle to secondBottomRight
turtle.goto(secondBottomRight)
#drop pen
turtle.pendown()
turtle.goto(firstBottomRight)

#keep window open after reaching last line
turtle.done()