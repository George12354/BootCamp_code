# To import a module, we can use the format👇
# import hangman_words
# from code_data import MENU, resources
# chosen_word = random.choice(hangman_words.word_list)
# or
# from hangman_words import word_list
# chosen_word = random.choice(word_list)
# import math
import random


# def greet(self, Profession):
#     print(f"Hello {self}")
#     print(f"How does it feel to be a {Profession}?")
#
#
# # from  line 8 to 10 the variable 'self' is a parameter
# # the 'input()' which is the actual data is called the argument
#
# greet(Profession="Damn Physicist", self="George")
# a = 49
# b = 8
# print(round(a / b))
# print(math.ceil(a / b))

# shift = int(input("input number: "))
# print(shift)
# shift_number = shift % 25
# print(shift_number)
# if shift > 25:
#     shift_number = shift - 25 - 1
#     print(shift_number)
# print(101 % 50)
# year = int(input("year"))
# print(int(input("year_1: ")) % 4)  # == 0
# print(int(input("year_2: ")) % 100)
# print(int(input("year_3: ")) % 400)

# Modifying Global Scope
# enemies = 1
#
#
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Brief sample on how to access the values in a dictionary(seems like a dictionary within a dictionary)

# Generate a random account from the game date.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format.
account_name = account_a["self"]
account_descr = account_a["description"]
account_country = account_a["country"]
print(f"{account_name}, a {account_descr}, from {account_country}")

print(MENU["espresso"]["ingredients"]["water"] - 21)
["cost"]
resources["water:"] - MENU["espresso"]["ingredients"]["water"], "ml"
resources["milk:"] - MENU["espresso"]["ingredients"]["milk"], "ml"
resources["coffee:"] - MENU["espresso"]["ingredients"]["coffee"], "g"

original_1 = resources["water:"]
original_2 = resources["milk:"]
original_3 = resources["coffee:"]
if original_1 > MENU["espresso"]["ingredients"]["water"] \
        and original_2 > MENU["espresso"]["ingredients"]["milk"] \
        and original_3 > MENU["espresso"]["ingredients"]["coffee"]:
    original_1 = resources["water:"] - MENU["espresso"]["ingredients"]["water"]
    original_2 = resources["milk:"] - MENU["espresso"]["ingredients"]["milk"]
    original_3 = resources["coffee:"] - MENU["espresso"]["ingredients"]["coffee"]
else:
    if original_1 < MENU["espresso"]["ingredients"]["water"]:
        print("Sorry there is not enough water")
    elif original_2 < MENU["espresso"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
    elif original_3 > MENU["espresso"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")

# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#
#
# # Creating an instance of MyClass
# obj = MyClass("John", 25)
#
# # Accessing attributes and calling methods
# obj.display_info()


# class Teacher:
#     # definition for init method or constructor
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
#
#     # Random member function
#     def show(self):
#         print(self.name, " teaches ", self.subject)
#
#
# T = Teacher('Preeti Srivastava', "Computer Science")  # init is invoked here
# T.show()


# Naming Case Convention
# Pascal Case; first of every letter will be capitalized
# camel Case: second down will be capitalized
# snake case: everything will be lower

# N.B: First line of code, the class--- Second line of code, the function attributes---
# Third line of code, the function and its name(method)
# Adding Methods to class and also working with attributes

# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#         # print(self.username)
#         # print(self.id)
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "angela")
# user_2 = User("002", "Jack")
# function that is attached to an object is called a method
# ***Observation: It seems like when calling a method, the object variable takes the place of the argument.

# user_2.follow(user_1)  # this part "user_2" which is the object, will represent the "self"
# print(user_1.followers)  # while "user_1" used as the argument, will represent the "user.followers"
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# Python quiz:

# def outer_func(x):
#     y = 1 + x
#
#     def inner_func():
#         x = 2
#
#         def inner_inner():
#             x = 3
#             return x + y
#
#         return inner_inner
#
#     return inner_func
#
#
# results = outer_func(4)
# my_results = results()
# print(my_results() + 2)
