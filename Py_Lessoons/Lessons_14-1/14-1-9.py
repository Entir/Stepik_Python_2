import turtle


def rmb(side):
    turtle.forward(side)
    turtle.left(60)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(60)
    turtle.forward(side)
    turtle.left(120)


for _ in range(10):
    turtle.right(36)
    rmb(100)
