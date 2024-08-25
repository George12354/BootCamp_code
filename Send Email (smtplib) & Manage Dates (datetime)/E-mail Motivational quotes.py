import random
import smtplib
import datetime as dt
import os

now = dt.datetime.now()
day_of_week = now.weekday()


file_list = []
with open("quotes.txt", "r") as file:
    data = file.readlines()
    file_data = [file_list.append(quote.strip("\n")) for quote in data]

# Retrieve email and password from environment variables
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


with smtplib.SMTP("smtp.gmail.com", timeout=10) as connection:
    # The line of code below provide a secure connection btw the email(if someone intercept the email, it encrypts
    # it.)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="geordie.e.ugo@gmail.com",
        msg=f"Subject: Wake up sleepy head\n\nDay: {day_of_week + 1}\n\n{file_list[random.randrange(len(file_list))]}."
    )

# To send your login details to your system env variable use this code on your terminal

# setx MY_EMAIL "your_email@example.com"
# setx MY_PASSWORD "your_password"
