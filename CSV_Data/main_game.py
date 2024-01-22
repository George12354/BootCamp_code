import turtle
from turtle import Turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
# This approach we took here is to load in a new image as a new shape.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
word = Turtle()
word.penup()
word.hideturtle()


# if you want to figure out the coordinate of each of the states.

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
correct_answer = []

states_to_learn = []
score = 0
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    data = pandas.read_csv("50_states.csv")
    U_S_states = data["state"].to_list()
    for guess in U_S_states:
        if guess == answer_state.title():
            correct_answer.append(answer_state)
            x_cor = data[data.state == guess]
            cor_x = int(x_cor.x)
            y_cor = data[data.state == guess]
            cor_y = int(y_cor.y)
            word.goto(x=cor_x, y=cor_y)
            word.write(guess, align="center", font=("Courier", 10, "bold"))
            if correct_answer.count(answer_state) == 1:
                score += 1
        if answer_state == "Exit":
            break

    # save the missing states to a .csv

    for inner in correct_answer:
        U_S_states.remove(inner.title())
    missed_ = {
        "States": U_S_states
    }
    missing_state = pandas.DataFrame(missed_)
    missing_state.to_csv("states_missed.csv")


# turtle.mainloop()
# mainloop, an alternative way of keeping the screen open even when the code has been executed.
