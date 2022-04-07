"""A beautiful playground."""

__author__ = "730397634"

from turtle import Turtle, done


def main() -> None:
    """Cpnstruct any Turtle objects and make use of all the functions called below."""
    playground: Turtle = Turtle()
    square(playground, 4, 5)
    octagon(playground, 6, 7)
    rectangle(playground, 3, 4)
    triangle(playground, 8, 4)
    done()
    

def square(seats: Turtle, side_one: float, side_two: float) -> None:
    """Square shapes to represent seats on a playground."""
    seats.goto(side_one, side_two)
    seats.pendown()
    seats.pencolor("green")
    
    seats.forward(150)
    
    i: int = 0
    while (i < 3):
        seats.left(90)
        seats.forward(100)
        i = i + 1
    seats.penup()


def octagon(merry: Turtle, side_one: float, side_two: float) -> None:
    """An octagon shape to represent a merry-go-round."""
    merry.goto(side_one, side_two)
    merry.pendown()
    merry.pencolor("blue")
    
    merry.forward(150)

    i: int = 0
    while (i < 6):
        merry.left(48.9)
        merry.forward(101)
        i = i + 1
    merry.penup()


def rectangle(slide: Turtle, side_one: float, side_two: float) -> None:
    """A rectangle shape to represent a slide at a playground."""
    slide.goto(side_one, side_two)
    slide.pendown()
    slide.begin_fill()
    slide.end_fill()
   
    slide.forward(300)
    slide.right(90)
    slide.forward(150)
    slide.right(90)
    slide.forward(300)
    slide.right(90)
    slide.forward(150)
    slide.right(90)

    slide.penup()


def triangle(shed: Turtle, side_one: float, side_two: float) -> None:
    """A triangle to represent a shed on the slide part of a playground."""
    shed.goto(side_one, side_two)
    shed.pendown()
    shed.pencolor("red")

    shed.forward(200)
    shed.left(120)
    shed.forward(200)
    shed.left(120)
    shed.forward(200)

    shed.penup()


def another_square(another_seat: Turtle, side_one: float, side_two: float) -> None:
    """Another Square shapes to represent another seat on a playground."""
    another_seat.goto(side_one, side_two)
    another_seat.pendown()
    another_seat.pencolor("green")
    
    another_seat.forward(150)
    
    i: int = 0
    while (i < 3):
        another_seat.left(90)
        another_seat.forward(100)
        i = i + 1
    another_seat.penup()


if __name__ == "__main__":
    main()
