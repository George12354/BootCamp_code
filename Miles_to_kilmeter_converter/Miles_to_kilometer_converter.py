from tkinter import *


def button_clicked():
    value = float(data.get())*1.609
    my_label_4.config(text=value)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=50, pady=25)

# Label
my_label = Label(text="Miles", font=("Ariel", 10, "bold"))
my_label.grid(column=2, row=0)
my_label.config(padx=5, pady=5)

my_label_2 = Label(text="is equal to", font=("Ariel", 10, "bold"))
my_label_2.grid(column=0, row=1)
my_label_2.config(padx=5, pady=5)

my_label_3 = Label(text="Km", font=("Ariel", 10, "bold"))
my_label_3.grid(column=2, row=1)
my_label_3.config(padx=5, pady=5)

my_label_4 = Label(text=0, font=("Ariel", 10, "bold"))
my_label_4.grid(column=1, row=1)
my_label_4.config(padx=5, pady=5)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)

# Entry
data = Entry(width=10)
data.grid(column=1, row=0)

window.mainloop()

