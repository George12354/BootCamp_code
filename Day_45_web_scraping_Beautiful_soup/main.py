# NB: BEFORE YOU SCRAPE A WEBSITE, ALWAYS GO TO THE ROOT OF THEIR URL AND CHECK OUT
#  THEIR robots.txt -----https://news.ycombinator.com/robots.txt
from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


article_title = soup.find_all(name="span", class_="titleline")
article_score = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]


article_text = []
article_links = []

for article_tag in article_title:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_text.append(text)
    article_links.append(link)


# check for highest number
score = 0
for no in article_score:
    if no > score:
        score = no
print(score)

list_index = article_score.index(score)
print(article_text[list_index])
print(article_links[list_index])

