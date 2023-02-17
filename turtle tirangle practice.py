import turtle
import math

turtle.penup()
turtle.setheading(90)
turtle.forward(50)
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(50)

turtle.left(116)

triangle_base = 50**2 + 100**2

turtle.forward(math.sqrt(triangle_base))

turtle.penup()

turtle.setheading(270)

turtle.goto(0, -50)

turtle.setheading(180)
turtle.forward(50)
turtle.pendown()
turtle.setheading(0)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)
turtle.right(154)
turtle.forward(math.sqrt(triangle_base))
turtle.goto(0, 50)
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.goto(50, -50)

turtle.done()
