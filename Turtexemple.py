import turtle

n = 0


def parallelogram(n=0):
    turtle.forward(100)
    turtle.right(110 + n)
    turtle.forward(100)
    turtle.right(70 + n)
    turtle.forward(100)
    turtle.right(110 + n)
    turtle.forward(100)
    turtle.right(70 + n)
    turtle.forward(100)


parallelogram(0)
turtle.left(110)
parallelogram(-180)
turtle.left(70)
turtle.forward(100)
turtle.left(70)
turtle.forward(100)
turtle.left(40)
turtle.forward(110)

turtle.done()
