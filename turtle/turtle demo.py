#import Turtle Graphics module
import turtle

#open Turtle window
#Turtle default position is center, facing 0 degrees (East)
turtle.showturtle()

#move Turtle forward by x pixles
turtle.forward(200)

#turning Turtle is done by using right(angle) or left(angle) method calls
#Compass directions:
#                   East: 0
#                   North: 90
#                   West: 180
#                   South: 270

#These instructions, following the initial 200 forward, should draw a perfect
#square on the Turtle page
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
