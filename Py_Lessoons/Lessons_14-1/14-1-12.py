import turtle


def square(side):
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)


for i in range(10, 301, 10):
    square(i)
