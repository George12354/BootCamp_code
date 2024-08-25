import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")

# h3 class = "title"
movie_title = soup.find_all(name="h3", class_="title")

score = 100
title_list = []
ordered_list = []

for title in movie_title:
    title_list.append(title.getText())

for order in title_list:
    score = score - 1
    ordered_list.append(title_list[score])

# This part is for the file
with open('movies.txt', 'w', encoding="utf-8") as file:
    for movies in ordered_list:
        file.write(movies + "\n")

print(title_list)
print(ordered_list)
