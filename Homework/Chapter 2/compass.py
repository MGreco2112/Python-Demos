#import Turtle module
import turtle

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

#keep window open after reaching last line
turtle.done()