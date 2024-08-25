from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Ariel"
BACKGROUND_FONT = "#B1DDC6"


# ---------------------------- BUTTON FUNCTION ------------------------------- #

def right_button():
    global list_no, data
    flip_front()
    english_word = data["English"].to_list()
    japanese_word = data["Japanese"].to_list()
    del english_word[list_no]
    del japanese_word[list_no]
    print(english_word)
    print(japanese_word)


def wrong_button():
    flip_front()


# ---------------------------- FLIP MECHANICS ------------------------------- #

def flip_back():
    global title, words, canvas, list_no

    title.config(text="English", bg="#91C2AF")

    data_1 = pandas.read_csv("data/Frequency_List.csv")
    english_word = data_1["English"].to_list()

    e_w = english_word[list_no]

    words.config(text=f"{e_w}", font=(FONT_NAME, 40, "bold"), bg="#91C2AF")

    # The front will take English
    canvas.config(bg=BACKGROUND_FONT)
    card_front_my_image.config(file="images/card_back.png")


def flip_front():
    global title, words, canvas, window, list_no

    title.config(text="Japanese")

    data_2 = pandas.read_csv("data/Frequency_List.csv")
    japanese_word = data_2["Japanese"].to_list()

    list_no = random.randrange(len(japanese_word))
    j_w_ = japanese_word[list_no]

    words.config(text=f"{j_w_}", font=(FONT_NAME, 60, "bold"))

    # The front will take Japanese

    card_front_my_image.config(file="images/card_front.png")
    window.after(5000, flip_back)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_FONT)

# The front will take japanese
canvas = Canvas(width=800, height=527, bg=BACKGROUND_FONT, highlightthickness=0)
card_front_my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_my_image)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
r_button = Button(image=right_image, highlightthickness=0, command=right_button)
r_button.grid(column=0, row=1, columnspan=1)

wrong_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_image, highlightthickness=0, command=wrong_button)
w_button.grid(column=1, row=1, columnspan=1)

title = Label(text="Japanese", font=(FONT_NAME, 40, "italic"), bg="white")
title.place(x=300, y=150)

data = pandas.read_csv("data/Frequency_List.csv")
japanese_words = data["Japanese"].to_list()
list_no = random.randrange(len(japanese_words))
j_w = japanese_words[list_no]

words = Label(text=f"{j_w}", font=(FONT_NAME, 60, "bold"), bg="white")
words.place(x=270, y=263)
window.after(5000, flip_back)

window.mainloop()
