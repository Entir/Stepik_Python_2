import turtle


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)


for _ in range(6):
    turtle.forward(100)
    turtle.left(60)
    hexagon(100)
