# import smtplib
#
# my_email = "pyth128@gmail.com"
# password = "gijc fnkb kgdh kobk"
#
# with smtplib.SMTP("smtp.gmail.com", timeout=10) as connection:
#     # The line of code below provide a secure connection btw the email(if someone intercept the email, it encrypts
#     # it.)
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pythsec650@gmail.com",
#         msg="Subject: Hello\n\nThis is the body of my email."
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(day)
day_of_week = now.weekday()
print(day_of_week + 1)
print(now)

date_of_birth = dt.datetime(year=2001, month=2, day=4)
print(date_of_birth)




