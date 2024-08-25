import turtle
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
tim.speed("fastest")
turtle.title("Etch-A-Sketch App")


def move_forward():
    tim.forward(10)


def move_downward():
    tim.backward(10)


def clear():
    tim.reset()


def anti_clockwise():
    tim.left(0)
    tim.circle(60, 90)
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    # tim.left(10.0)


def clockwise():
    tim.setheading(180)
    tim.circle(60, 90)
    # format Angela used:
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    # tim.right(10.0)


my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_downward)
my_screen.onkey(key="c", fun=clear)
my_screen.onkey(key="a", fun=anti_clockwise)
my_screen.onkey(key="d", fun=clockwise)
my_screen.exitonclick()
