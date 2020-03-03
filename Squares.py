# Casandra Villagran
# 03/2/2020

# Use the following chunk of code to produce the image shown below.


import turtle
def drawSquare (t, size):
    for i in range (4):
        t.forward(size)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor('white')
    pat = turtle.Turtle()
    pat.pensize(2)
    pat.speed(10)
    pat.color('blue')
    space = -10

    for i in range(20, 105, 20):
        drawSquare(pat,i)
        pat.up()
        pat.goto(space, space)
        pat.down()
        space = space - 10
    wn.exitonclick()
main()
