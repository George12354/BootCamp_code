from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=data.get())


# window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# To add a padding, can also be done for other widget in the same format.
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Ariel", 24, "bold"))
# Different option of calling the tkinter attribute.
# my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(column=0, row=0)
# NB: if you want sth to appear on screen use the pack attribute.


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button")
# button.pack()
new_button.grid(column=2, row=0)


# Entry
data = Entry(width=10)
# print(data.get())
# data.pack()
data.grid(column=3, row=2)

# NB: There are about three main(probably more) layout managers such as: pack(),grid() and place()--place is precise
# and works with a coordinate system.
window.mainloop()
