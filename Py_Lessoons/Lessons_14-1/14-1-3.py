import turtle


def triangle(side):
    turtle.right(60)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)


triangle(200)
