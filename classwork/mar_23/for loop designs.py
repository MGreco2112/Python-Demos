import turtle

NUM_CIRCLES = 10
RADIUS = 100
ANGLE = 10

for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()