import requests
from datetime import datetime
from twilio.rest import Client

# US4ecd49c2163025dbd4cf21779dbf0145
account_sid = ""
auth_token = ""

stock_price_API = "QTF506T19UAN1YBO"
news_API = "011062d077ad485a9b6610af2bc31d3a"


now = datetime.now()
month = str(now.month)
year = str(now.year)
yesterday = str(now.day - 1)
daybfour = str(now.day - 2)


date_format = "%Y-%m-%d"

date_string_yesterday = f"{year}-{month}-{yesterday}"
date_string_daybfour = f"{year}-{month}-{daybfour}"

parsed_date_0 = datetime.strptime(date_string_yesterday, date_format)
parsed_date_1 = datetime.strptime(date_string_daybfour, date_format)

date_part_0 = parsed_date_0.strftime("%Y-%m-%d")
date_part_1 = parsed_date_1.strftime("%Y-%m-%d")


STOCK_PRICE_Endpoint = ('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY'
                        '&apikey=stock_price_API')
NEWS_Endpoint = "https://newsapi.org/v2/top-headlines"

response = requests.get(STOCK_PRICE_Endpoint)
response.raise_for_status()
stock_data = response.json()


yesterday_stock = float(stock_data["Time Series (Digital Currency Daily)"][date_part_0]["4b. close (USD)"])
daybfour_stock = float(stock_data["Time Series (Digital Currency Daily)"][date_part_1]["4b. close (USD)"])
# abs() helps to get the positive difference btw two numbers, Returns the absoluter value of a number.

diff_in_stock = yesterday_stock - daybfour_stock
percentage_diff = round(diff_in_stock / yesterday_stock * 100, 1)


print(f"BTC yesterday {yesterday_stock}")
print(f"BTC daybfour {daybfour_stock}")
print(percentage_diff)


# Now let's work on the news part.
news_parameter = {
    "country": "us",
    "q": "Crypto",
    "apikey": news_API,
    "category": "business"
}

news_call = requests.get(NEWS_Endpoint, params=news_parameter)
news_call.raise_for_status()
news_data = news_call.json()
print(news_data["articles"][:3])
headline = news_data["articles"][:3]
news_headline = ""
news_description = ""

#   This part is for the sms
trend_sign = ""

if percentage_diff > 0:
    trend_sign = "💹💲"
else:
    trend_sign = "🔻💲"

for story in headline:
    news_headline = story["title"]
    news_description = story["content"]

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"Sent from your Twilio trial account-\n"
                 f"BTC{trend_sign} {percentage_diff}%.\n"
                 f"Headline: {news_headline} \n"
                 f"Description: {news_description}",
            from_='the number generated from twilio',
            to='08147454714'
        )
    print(message.status)
