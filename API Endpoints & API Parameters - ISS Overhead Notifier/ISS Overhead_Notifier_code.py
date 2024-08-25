from datetime import datetime
import time
import requests
import smtplib

MY_LAT = 32.715736  # Your latitude
MY_LONG = -117.161087  # Your longitude
my_email = "pyth128@gmail.com"
password = "gijc fnkb kgdh kobk"


# Your position is within +5 or -5 degrees of the ISS position.
def position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LAT >= iss_latitude - 5 and MY_LAT >= iss_latitude + 5:
        if MY_LONG >= iss_longitude - 5 and MY_LONG >= iss_longitude + 5:
            # print("seems like the damn code is working")
            # print(iss_longitude, iss_latitude)
            return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now().hour

# If the ISS is close to my current position,
# and it is currently dark
while True:
    time.sleep(60)
    if time_now >= 16:
        position()

        with smtplib.SMTP("smtp.gmail.com", timeout=10) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="pythsec650@gmail.com",
                msg=f"Subject: Wake up sleepy head\n\n Go outside and look up. "
            )

# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
