"""Creating a turtle scene."""
from turtle import Turtle, colormode, done

bob: Turtle = Turtle()
bob.pencolor("black")
bob.fillcolor(43, 41, 46)
bob.color("red", "blue")

bob.forward(300)
bob.left(90)
bob.forward(300)
bob.left(90)
bob.forward(300)
bob.left(90)
bob.forward(300)
bob.left(90)

bob.penup()
bob.goto(45, 60)
bob.pendown()

bob.speed(70)

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(121.5)
    i = i + 1
    
side_length = side_length * 0.97