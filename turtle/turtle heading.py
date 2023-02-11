import turtle

#specific heading with Turtle
#turtle.setheading(angle) specifies an exact heading for the Turtle

#lift pen
turtle.penup()
#point north
turtle.setheading(90)
#move north 200px
turtle.forward(200)
#pen down
turtle.pendown()
#draw 400x400px square
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(270)
turtle.forward(400)
turtle.setheading(180)
turtle.forward(400)
turtle.setheading(90)
turtle.forward(400)
turtle.setheading(0)
turtle.forward(200)
#create inner divisions, red ink
turtle.pencolor("red")
turtle.setheading(270)
turtle.forward(200)
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(180)
turtle.forward(400)
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(270)
turtle.forward(200)
#position for diagonal divisions
turtle.setheading(0)
turtle.forward(200)
#botton right to top right division
turtle.pencolor("yellow")
turtle.setheading(135)
turtle.forward(565)
#position for second diagonal
turtle.setheading(0)
turtle.forward(400)
#top right to bottom left division
turtle.setheading(225)
turtle.forward(565)
#position to divide quadrents in half
turtle.setheading(0)
turtle.forward(100)
#left quads division
turtle.pencolor("orange")
turtle.setheading(90)
turtle.forward(400)
#position for right quadrents
turtle.setheading(0)
turtle.forward(200)
#right quads division
turtle.pencolor("blue")
turtle.setheading(270)
turtle.forward(400)
#position for quadrent alternate diagonal division
turtle.setheading(180)
turtle.forward(100)
#divide bottom right to top left
turtle.pencolor("black")
turtle.right(45)
turtle.forward(282)
#divide bottom left to top right
turtle.right(90)
turtle.forward(282)
#divide top left to bottom right
turtle.right(90)
turtle.forward(282)
#divide top right to bottom left
turtle.right(90)
turtle.forward(282)
#reset to center screen
turtle.penup()
turtle.goto(-100,100)
#circle, center screen
turtle.pendown()
turtle.pencolor("green")
turtle.circle(70)
