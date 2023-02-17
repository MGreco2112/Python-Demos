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

#generate a square of 100 x 100px
for x in range(4):
    turtle.forward(100)
    turtle.right(90)

#rotate turtle by 45 degrees for diagonal division
turtle.right(45)

#determine a squared and b squared of triangle legs, add together
sqrt = 100**2 + 100**2

#move turtle forward the square root of a squared plus b squared
turtle.forward(math.sqrt(sqrt))

#position turtle on opposing end of square
turtle.left(135)
turtle.forward(100)
turtle.left(135)
#bisect square utilizing the square root of a squared plus b squared
turtle.forward(math.sqrt(sqrt))
#position turtle at center position of eastern most side of square
turtle.right(135)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)

#determine a squared plus b squared of triangles half the size of currently created triangles
sqrt = 50**2 + 50**2

#turn turtle left at the appropriate angle to create these triangles
turtle.left(135)
#move turtle forward the square root of newly declaired a squared plus b squared
turtle.forward(math.sqrt(sqrt))

#move angle turtle and contine forward movement at that rate
for x in range(3):
    turtle.left(90)
    turtle.forward(math.sqrt(sqrt))

#inscribed circle created at central position of northern most side of square, radius half the length and height of square
turtle.left(45)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.circle(50)
#circumscribed created at north western point of square, angled inwards 45 degrees at radius of the square root of
#the length and width squared of the large square
turtle.forward(50)
turtle.left(45)
sqrt = 100**2 + 100**2
turtle.circle(math.sqrt(sqrt) / 2)

turtle.done()