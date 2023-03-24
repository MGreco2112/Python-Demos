import turtle

radius = 10
y_pos_mod = 0
X_POS = 0

for cir in range(20):
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    radius += 10
    y_pos_mod -= 10
    turtle.goto(X_POS, y_pos_mod)


turtle.done()
