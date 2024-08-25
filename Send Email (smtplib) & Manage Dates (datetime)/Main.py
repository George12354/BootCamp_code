# compare csv data(date) with current date and time
# access letter template(randomized) and input csv data (name) into text file
# retrieve the intended email from csv and send to the recipient.
import csv
import random
import smtplib
import datetime as dt
import os


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# Execute While statement here
num = random.randint(1, 3)

with open(f"letter_templates/letter_{num}.txt", "r") as file:
    template = file.read()
    # print(template)

    with open("birthdays.csv", 'r') as data:
        # Create a CSV reader object for dictionaries
        csv_reader = csv.DictReader(data)

        for row in csv_reader:
            # Check if the name is Angela
            if row["year"] == str(year) and row["month"] == str(month) and row["day"] == str(day):

                my_email = os.environ.get("MY_EMAIL")
                password = os.environ.get("MY_PASSWORD")

                with open("ReadyToSend.txt", "w") as fill:
                    new_g = template.replace("[NAME]", f"{row['name']}")
                    fill.write(new_g)
                with open("ReadyToSend.txt", "r") as card:
                    content = card.read()
                    birthday_card = content.strip("\n")

                with smtplib.SMTP("smtp.gmail.com", timeout=10) as connection:

                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=f"{row['email']}",
                        msg=f"Subject: Happy Birthday🎉 \n\n{birthday_card}".encode('utf-8')
                    )
