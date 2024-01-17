import turtle


def square(side):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)


for _ in range(8):
    turtle.left(45)
    square(100)
