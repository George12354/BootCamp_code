from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '.', '-', '_', '@', '#', '$', '%', '&', '*']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    # Python string join() Method
    # join all items in a tuple into a string, using ""
    pass_word = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {pass_word}")
    password_entry.insert(index=0, string=f"{pass_word}")
    pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    # code below creates a pop-up dialogue

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            # Here we focus on write, read and update JSON date
            with open("data.json", "r") as data_file:
                # This code to update, involves different steps.
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        except ValueError:
            print("file not found")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        # This code to read
        # data = json.load(data_file)
        # print(data)
        # This code to write
        # json.dump(new_data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            for website in data:
                if website_entry.get() == website:
                    messagebox.showinfo(title=website_entry.get(),
                                        message=f"Email: {data[website_entry.get()]['email']}\n "
                                                f"PassWord: {data[website_entry.get()]['password']}")
                else:
                    messagebox.showwarning(title="Error", message=f"No details for {website_entry.get()} exists.")
    except ValueError:
        messagebox.showwarning(title="Oops", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="black")
key_lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_lock_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Courier", 10, "bold"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search_button = Button(text="search", font=("Courier", 10, "bold"), width=17, command=find_password,
                       highlightthickness=0)
search_button.grid(column=2, row=1, columnspan=2)

email_name = Label(text="Email/Username: ", font=("Courier", 10, "bold"))
email_name.grid(column=0, row=2)
email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(index=0, string="example@gmail.com")

password = Label(text="Password: ", font=("Courier", 10, "bold"))
password.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=1)

generator_button = Button(text="Generate Password", font=("Courier", 10, "bold"), command=generate_password,
                          highlightthickness=0)
generator_button.grid(column=2, row=3, columnspan=2)

click_add_button = Button(text="Add", width=51, command=save)
click_add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
