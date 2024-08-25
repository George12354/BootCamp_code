# Angela wrote this code, can't take the credit.
import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
turtle.title("Turtle Race")
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-160, -100, -30, 30, 100, 160]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y[turtle_index])
    all_turtle.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:

    for timmy in all_turtle:
        if timmy.xcor() > 230:
            is_race_on = False
            winning_color = timmy.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        timmy.forward(rand_distance)

my_screen.exitonclick()
