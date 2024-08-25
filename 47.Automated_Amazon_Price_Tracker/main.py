import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Write your code below this line 👇

load_dotenv()  # take environment variables from .env.
practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US"

# headers = {'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
#            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                          "Chrome/126.0.0.0 Safari/537.36",
#            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
#                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#            "Accept-Encoding": "gzip, deflate, br, zstd",
#            "Priority": "u=0, i",
#            "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
#            "Sec-Ch-Ua-Mobile": "?0",
#            "Sec-Ch-Ua-Platform": "\"Windows\"",
#            "Sec-Fetch-Dest": "document",
#            "Sec-Fetch-Mode": "navigate",
#            "Sec-Fetch-Site": "cross-site",
#            "Sec-Fetch-User": "?1",
#            "Upgrade-Insecure-Requests": "1"}

response = requests.get(url=live_url)
Amazon_web_page = response.text

soup = BeautifulSoup(Amazon_web_page, "html.parser")

# print(soup.prettify())

price_tag = soup.find(class_="a-offscreen")

print(price_tag)
price_tag_str = price_tag.getText().strip("$")
price_tag_str_float = float(price_tag_str)
print(f"${price_tag_str_float}")

print(soup.prettify())

# The product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# This section is for the Email

message = f"{title} is on sale for ${price_tag_str_float}!"

if price_tag_str_float < 100:
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("MY_PASSWORD")

    print(f"Email: {my_email}")  # Should print your email address
    print(f"Password: {'*' * len(password) if password else None}")  # Should print asterisks for your password
    # length or None

    # Retrieve email and password from environment variables

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        # The line of code below provide a secure connection btw the email(if someone intercept the email, it encrypts
        # it.)
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["SENDER_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode("utf-8")
        )
