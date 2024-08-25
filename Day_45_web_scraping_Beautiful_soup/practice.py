from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)  # gets text with tag
print(soup.title.text)  # strip tags

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

all_anchor_tags = soup.findAll(name='a')  # findAll gets all the tags that match the parameter

id_is_name = soup.find(id="name")
print(id_is_name)

for tag in all_anchor_tags:
    print(tag.getText())  # getText strips the tag and prints the text
    print(tag.get('href'))  # .get() gets any attribute passed as a parameter

head = soup.find(name='h1', id='name')  # Find specific text based on tag AND id -- can also use 'class_'
section_heading = soup.find(name='h3', class_='name')  # Find specific text based on tag AND id -- can also use 'class_'
print(section_heading.getText())  # To get the text
print(section_heading.name)  # To know the name of that particular tag.
print(section_heading.get("class"))  # To get the value of an attribute


# All matching items - example: use dot for class
company_url = soup.select(selector=".heading")

# First matching item - can use css,  id -> #id-text-goes here, class
company_url = soup.select_one(selector="p a")

name = soup.select_one("#name")
print(name)
