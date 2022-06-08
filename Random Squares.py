import random
import turtle
turtlepen = turtle.Pen()

turtlepen.shape("turtle")
turtlepen.width(5)
turtlepen.speed(0)

colorlist = ["blue", "red", "green", "yellow", "purple", "pink"]

def square(size):
    for i in range(4):
        turtlepen.forward(size)
        turtlepen.left(90)

infiniteloop = 1

while infiniteloop == 1:
    for i in range(100):
        x = random.randrange(-400, 400)
        y = random.randrange(-400, 400)
        turtlepen.up()
        turtlepen.goto(x, y)
        turtlepen.down()
        squaresize = random.randrange(10,200)
        colour = random.choice(colorlist)
        turtlepen.color(colour)
        square(random.randrange(10,200))
        
    
