from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)


leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.color(99, 204, 250)

leo.begin_fill()
leo.end_fill()

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
bob.pencolor("black")
bob.fillcolor(43, 41, 46)
bob.color("red", "blue")

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