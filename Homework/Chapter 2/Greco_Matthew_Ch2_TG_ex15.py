#import Turtle Graphics
import turtle

#set Turtle to move without drawing
turtle.penup()
#move Turtle to 50 pixels to the left and 50 pixels up on the grid
turtle.goto(-50, 50)
#set Turtle to draw when moved
turtle.pendown()
#turn Turtle to face the East
turtle.setheading(0)
#move Turtle forward 100px
turtle.forward(100)
#turn Turtle to the south
turtle.right(90)
turtle.forward(100)
#turn Turtle to the West
turtle.right(90)
turtle.forward(100)
#turn Turtle to the North
turtle.right(90)
turtle.forward(100)
#position Turtle for circle draw
turtle.setheading(223)
#set Turtle to fill red
turtle.fillcolor("red")
#activate filling
turtle.begin_fill()
#draw Circle radius 80px
turtle.circle(80)
#end filling
turtle.end_fill()

#keeps Turtle window open after execution finishes
turtle.done()