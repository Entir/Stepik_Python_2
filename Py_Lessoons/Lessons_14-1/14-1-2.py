import turtle

def rectangle(width: int, height: int):
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width + width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(0)
    turtle.forward(width)

if __name__ == '__main__':
    rectangle(200, 100)
