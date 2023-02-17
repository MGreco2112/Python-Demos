import turtle
import math

# #assignemnt 1
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# #assignemnt 2
# turtle.forward(100)
# turtle.left(135)
# turtle.forward(100)

# # assignment 3
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(75)

# turtle.reset()


# turtle.right(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(75)

#assignemnt 4
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)

#assignment 5

for x in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.right(45)

sqrt = 100**2 + 100**2

turtle.forward(math.sqrt(sqrt))

turtle.left(135)
turtle.forward(100)
turtle.left(135)
turtle.forward(math.sqrt(sqrt))
turtle.right(135)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)

sqrt = 50**2 + 50**2

turtle.left(135)
turtle.forward(math.sqrt(sqrt))

for x in range(3):
    turtle.left(90)
    turtle.forward(math.sqrt(sqrt))



turtle.done()