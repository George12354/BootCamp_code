# from art import logo

# Day 7 project(Hangman)
import random

from ASCII_Art import vs
from code_data import data, resources, MENU

#
# from hangmaon_art import logo, stages
#
# print(logo)
# word = ["sleep", "python", "gone"]
# chosen_word = random.choice(word)
# print(f"Pssst, the solution is {chosen_word}")
#
# display = []
# for i in range(len(chosen_word)):
#     display.append('_')
#
# # check guessed letter
# lives = 6
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"Wrong guess, you have {lives} attempts left")
#     if "_" not in display:
#         print("You've won🎉🎉")
#     if lives == 0:
#         print("Game Over😌")
#         break
#     print(stages[lives])
#     print(display)
#     continue


#
#
# # Day 8.1 (Paint Area Calculator)
#   import math
# def area_calculator(height, width, wall_area):
#     area = height * width
#     num_of_paint = math.ceil(area / wall_area)
#     print(f"The number of paints to use is {num_of_paint}")
#
#
# # Note: To round up a number we import math and then use math.ceil(Dont forget)
# # Note: To round down a number use round(number)
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# area_calculator(height=test_h, width=test_w, wall_area=coverage)
#
#
# # Prime number checker
# def prime_checker():
#     n = int(input("Check this number: "))
#     if n > 1:
#         for i in range(2, int(n / 2) + 1):
#             if (n % i) == 0:
#                 print(f"{n} is not a prime number")
#                 break
#             else:
#                 print(f"{n} is a prime number")
#     else:
#         print(f"{n}is not a prime number")
#
#
# prime_checker()

# or you can use a different approach

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number - 1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It is a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# n = int(input("Enter to check if prime or not : "))
# prime_checker(number=n)

# Day 8.2 (Caesar Cipher)
# def encrypt():
#     # In this code I made an error of making the variable display, instead of as a string variable.
#     # wonder why it # # didn't work as a list ?
#     display = ""
#     for position in range(len(alphabet)):
#         for txt in text:
#             if txt == alphabet[position]:
#                 # for txt in alphabet[position]:
#                 new_number = position + shift
#                 display += alphabet[new_number]
#             print(display)


# def caesar(plain_text, shift_number, direction_path):
#     display = str(" ")
#     for letter in plain_text:
#         if letter not in alphabet:
#             display += letter
#         else:
#             if letter in alphabet:
#                 number = alphabet.index(letter)
#                 if direction_path == "encode":
#                     sum_shift = number + shift_number
#                     display += alphabet[sum_shift]
#
#                 else:
#                     if direction_path == "decode":
#                         sum_shift = number - shift_number
#                         display += alphabet[sum_shift]
#     print(f"The {direction_path}d text is {display}")
#
#
# def game():
#     continuum = True
#     while continuum:
#         end_ = (input("Type 'yes' if you want to go again. Otherwise, type 'no'."))
#         if end_ == "yes":
#             direction_sub = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#             text_sub = input("Type your message:\n").lower()
#             shift_sub = int(input("Type the shift number:\n"))
#             if shift_sub > 25:
#                 shift_sub = shift_sub % 25
#                 # print(shift)
#             caesar(plain_text=text_sub, shift_number=shift_sub, direction_path=direction_sub)
#             continue
#         else:
#             if end_ == "no":
#                 print("Good Bye")
#                 break
#
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']
#
# # from art import logo
# # print(logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# if shift > 25:
#     shift = shift % 25
#     # print(shift)
# caesar(plain_text=text, shift_number=shift, direction_path=direction)
# game()

# Day 9 _Dictionaries, Nesting and the Secret Auction
# programming_dictionary = {"Bug": " An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           "Loop": "The action of doing somethings over and over again."}

# Retrieving items from dictionary.
# print(programming_dictionary["Function"])

# Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Create an empty dictionary.
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer. "
# print(programming_dictionary)

# Loop through a dictionary
# Note: The variable "key" takes in the keys such as Bug, Loop, and Function.
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
# coding exercise on Grading program
# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grade = {}
# # write code below to add the grades to student_grade
# for name in student_score:
#     if student_score[name] >= 91:
#         student_grade[name] = "Outstanding"
#     elif student_score[name] >= 81:
#         student_grade[name] = "Exceeds Expectations"
#     elif student_score[name] >= 71:
#         student_grade[name] = "Acceptable"
#     elif student_score[name] <= 70:
#         student_grade[name] = "Fail"
# print(student_grade)
# Nesting
# capitals = {"France": "Paris",
#             "Germany": "Berlin",
#             }
# Nesting a list in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# List_in_list = ["A", "B", ["C", "D"]]
# Nesting Dictionary in a Dictionary
# travel_ = {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
# }
# travel_log = {
#     "France": travel_,
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# print(travel_log)
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12, },
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 5, }
# }
# print(travel_log)
# # Nesting Dictionary in a list
# travel_log = [
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visited": 12,
#      },
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visited": 5,
#      }
# ]


# def add_new_country(country_):
#     travel_log.append(country_)
#
#
# add_new_country(country_={"country": "Russia",
#                           "total_visited": 2,
#                           "cities_visited": ["Moscow", "Saint Petersburg"]
#                           })
# print(travel_log)


# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {"country": country_visited, "total_visited": times_visited, "cities_visited": cities_visited}
#     travel_log.append(new_country)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Secret Auction program
# auction_active = True
# while auction_active:
#     print("Welcome to the secret Auction program.")
#     name = input("What is your name? : ")
#     bid_amount = int(input("What's your bid? : "))
#     auction = {name: bid_amount}
#     roll_over = input("Are there any other bidders? Type 'yes' or 'no'")
#     while roll_over == "yes":
#         print("Welcome to the secret Auction program.")
#         name = input("What is your name? : ")
#         bid_amount = int(input("What's your bid? : "))
#         auction[name] = bid_amount
#         roll_over = input("Are there any other bidders? Type 'yes' or 'no'")
#     else:
#         if roll_over == "no":
#             index = 0
#             winner = ""
#             for customer in auction:
#                 if auction[customer] > index:
#                     index = auction[customer]
#                     winner = customer
#             print(f"The winner is {winner} with a bid of {index}")
#             print("bye")
#             # Am supposed to import some kind clear function
#             break


# Day 10 ; Functions with output
# def format_name(f_name, l_name):
#     # Below is an example of a Docstring.
#     """Take a first and last name and format it to return the title case version of the name. """
#     if f_name == " " or l_name == "":
#         return "You didn't provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"
#
#
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# # Days in Month
# def is_leap(year_s):
#     if year_s % 4 == 0:
#         if year_s % 100 == 0:
#             if year_s % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year_s, month_s):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     months = ["January", "February", "March", "April", "May", "June", "July", "August",
#               "September", "October", "November", "December"]
#     if is_leap(year_s):
#         month_days[1] += 1
#         return f"The number of days in the month of {months[month_index - 1]} is {month_days[month_s - 1]} days "
#     elif not is_leap(year_s):
#         return f"The number of days in the month of {months[month_index - 1]} is {month_days[month_s - 1]} days "
#
#
# year = int(input("Enter a year: "))
# month_index = int(input("Enter a month: "))
# days = days_in_month(year_s=year, month_s=month_index)
# print(days)

# Docstring This is a way to create a little bit of documentation as we are coding in our functions or in our other
# blocks of codes i.e. to document function.
# for an example on a Docstring, please visit line

# Calculator

# Add
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiplication(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# operations = {"+": add, "-": subtract, "*": multiplication, "/": division}
#
# # def calculator():
# print(logo)
# num1 = float(input("What's the first number?: "))
#
# go_again = True
# while go_again:
#     op = str(input("Pick an operation: "))
#     num2 = float(input("What's the next number?: "))
#     for sign in operations:
#         function = operations[sign]
#         if sign == op:
#             result = function(num1, num2)
#             print(result)
#             again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
#             if again == "y":
#                 num1 = result
#                 continue
#             else:
#                 if again == "n":
#                     # go_again = False
#                     # calculator()
#                     num1 = int(input("What's the first number?: "))
#                     continue
# Recursion : This is calling a function within its own definition
# calculator()


# Day 11 --The Blackjack Capstone Project
# play = True
# while play:
#     play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
#     if play_game == "y":
#         from Black_jack_art import logo
#
#         print(logo)
#         cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#         i = 0
#         a = 0
#         your_card = []
#         computer_card = []
#         your_total = 0
#         computer_total = 0
#         while i < 2:
#             your_card.append(random.choice(cards))
#             your_total += your_card[i]
#             i += 1
#         while a < 2:
#             computer_card.append(random.choice(cards))
#             computer_total += computer_card[a]
#             a += 1
#         print(f"Your cards: {your_card}, current score: {your_total}")
#         print(f"Computer's first card: {computer_card[0]}")
#         another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if another_card == "y":
#             if your_total < 17:
#                 i = 2
#                 your_card.append(random.choice(cards))
#                 your_total += your_card[i]
#                 print(f"Your cards: {your_card}, current score: {your_total}")
#                 print(f"Computer's first card: {computer_card[0]}")
#             if computer_total < 17:
#                 a = 2
#                 computer_card.append(random.choice(cards))
#                 computer_total += computer_card[a]
#         print(f"Your final hand: {your_card}, final score: {your_total}")
#         print(f"Computer's final hand: {computer_card}, final score: {computer_total}")
#         if your_total == computer_total:
#             print("Draw")
#         elif computer_total == 21:
#             print("Lose, opponent has Blackjack")
#         elif your_total == 21:
#             print("Win with a Blackjack")
#         elif your_total > 21:
#             print("You went over. You lose")
#         elif computer_total > 21:
#             print("Opponent went over. You win")
#         elif your_total > computer_total:
#             print("You win")
#         else:
#             print("You lose")
#
#     else:
#         if play_game == "n":
#             play = False
# This is the end of the Blackjack program, there might be some error in the condition for the rules of the game


# Day 12 - Scope _ Number Guessing Game-- Local scope# They exist within functions Global# What if we wanted it to be
# accessible outside the function? Well, now we need to think about something called global scope. The only
# difference between global scope and local scope is where you define. And global variables are available within,
# and it's also available outside of functions. Namespace# This concept of global and local scope doesn't just apply
# to variables. As I alluded to before, it also applies to functions and basically anything else you name. This is a
# concept called the Namespace.
# Note: The most important thing to remember from this is if you create a variable#
# within a function, then it's only available within that function.But if you create a variable within an if block or
# a while loop or a for loop or anything that has the indentation and the colon, then that does not count as creating
# a separate local scope.
# Modifying Global Scope
# enemies = 1


# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Final Project The Number Guessing Game

# print("Welcome to the Number Guessing Game! ")
# chosen_word = random.randint(1, 100)
# levels = input("I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
#
#
# def game_levels(attempt):
#     while attempt > 0:
#         print(f"You have {attempt} attempts remaining to guess the number.")
#         attempt -= 1
#         guess = int(input("Make a guess: "))
#         if guess > chosen_word:
#             print("Too high.")
#             print("Guess again")
#             continue
#         elif guess < chosen_word:
#             print("Too low.")
#             continue
#         elif guess == chosen_word:
#             print(f"You got it! The answer was {chosen_word}.")
#             break
#     else:
#         if attempt == 0:
#             print(f"You've run out of guesses, you lose.\nThe chosen number was {chosen_word}")
#
#
# if levels == "easy":
#     game_levels(attempt=10)
# else:
#     if levels == "hard":
#         game_levels(attempt=5)


# Day 13 -- Debugging
# Describe the bug
# def my_function():
#     for i in range(1, 21):
#
#         if i == 20:
#             print("You got it")
#
#
# my_function()
#
# # Play Computer
# year = int(input("What's your year of birth? "))
# if 1980 <= year <= 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
#
# # Print is Your Friend
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#
#
# def mutate(a_list):
#     b_list = []
#     for i in range(len(a_list)):
#         new_item = a_list[i] * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
#     print("This is an even number. ")
# else:
#     print("This is an odd number. ")

# Debugging FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# Day 14 Higher Lower Game
# print(logo)
# score = 0
# game_on = True
# select_A = random.choice(data)
# select_B = random.choice(data)
# while game_on:
#     fact = []
#     for more in select_A:
#         fact.append(more)
#     name = str(fact[0])
#     follower_count = fact[1]
#     description = str(fact[2])
#     country = str(fact[3])
#     print(f"Compare A: {select_A[name]}, a {select_A[description]}, from {select_A[country]} ")
#     print(vs)
#
#     fact_B = []
#     for more_B in select_B:
#         fact_B.append(more_B)
#     name_B = str(fact[0])
#     follower_count_B = fact[1]
#     description_B = str(fact[2])
#     country_B = str(fact[3])
#     print(f"Against B: {select_B[name]}, a {select_B[description]}, from {select_B[country]} ")
#
#     followers = input("Who has more followers? Type 'A' or 'B':").upper()
#
#     if followers == "A" and select_A[follower_count] > select_B[follower_count]:
#         score += 1
#         select_A = select_A
#         select_B = random.choice(data)
#         print(f"You're right! Current score: {score} ")
#     elif followers == "B" and select_B[follower_count] > select_A[follower_count]:
#         score += 1
#         select_A = select_B
#         select_B = random.choice(data)
#         print(f"You're right! Current score: {score} ")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score} ")
#         game_on = False


# Day 15-- coffee-machine
# coffee_on = True
# profit = 0
# change = 0
# while coffee_on:
#     order = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     drink = []
#
#     # This part is for espresso
#     if order == "espresso":
#         print("Please insert coins.")
#         quarters = float(input("How many quarters?:"))
#         nickels = float(input("How many nickels?:"))
#         dimes = float(input("How many dimes?:"))
#         pennies = float(input("How many pennies?:"))
#         cost = 1.5
#         profit += cost
#         total_cash = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
#         if resources["water:"] >= MENU["espresso"]["ingredients"]["water"] \
#                 and resources["coffee:"] >= MENU["espresso"]["ingredients"]["coffee"]:
#             resources["water:"] -= MENU["espresso"]["ingredients"]["water"]
#             resources["coffee:"] -= MENU["espresso"]["ingredients"]["coffee"]
#             if total_cash > cost:
#                 print(f"Here is ${round(total_cash - cost, 2)} in change.")
#                 print("Here is your espresso☕️ Enjoy!")
#             elif total_cash == cost:
#                 print("Here is your espresso Enjoy!")
#             elif total_cash < cost:
#                 print("Sorry that's  not enough money. Money refunded.")
#         else:
#             if resources["water:"] < MENU["espresso"]["ingredients"]["water"]:
#                 print("Sorry there is not enough water")
#             elif resources["coffee:"] < MENU["espresso"]["ingredients"]["coffee"]:
#                 print("Sorry there is not enough coffee")
#
#         #     This part is for latte
#     elif order == "latte":
#         print("Please insert coins.")
#         quarters = float(input("How many quarters?:"))
#         dimes = float(input("How many dimes?:"))
#         nickels = float(input("How many nickels?:"))
#         pennies = float(input("How many pennies?:"))
#         cost = 2.5
#         profit += cost
#         total_cash = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
#         if resources["water:"] >= MENU["latte"]["ingredients"]["water"] \
#                 and resources["coffee:"] >= MENU["latte"]["ingredients"]["coffee"] \
#                 and resources["milk:"] >= MENU["latte"]["ingredients"]["milk"]:
#             resources["water:"] -= MENU["latte"]["ingredients"]["water"]
#             resources["milk:"] -= MENU["latte"]["ingredients"]["milk"]
#             resources["coffee:"] -= MENU["latte"]["ingredients"]["coffee"]
#             if total_cash > cost:
#                 print(f"Here is ${round(total_cash - cost, 2)} in change.")
#                 print("Here is your latte☕️ Enjoy!")
#             elif total_cash == cost:
#                 print("Here is your latte Enjoy!")
#             elif total_cash < cost:
#                 print("Sorry that's  not enough money. Money refunded.")
#         else:
#             if resources["water:"] < MENU["latte"]["ingredients"]["water"]:
#                 print("Sorry there is not enough water")
#             elif resources["milk:"] < MENU["latte"]["ingredients"]["milk"]:
#                 print("Sorry there is not enough milk")
#             elif resources["coffee:"] < MENU["latte"]["ingredients"]["coffee"]:
#                 print("Sorry there is not enough coffee")
#
#     #         This part is for cappuccino
#     elif order == "cappuccino":
#         print("Please insert coins.")
#         quarters = float(input("How many quarters?:"))
#         dimes = float(input("How many dimes?:"))
#         nickels = float(input("How many nickels?:"))
#         pennies = float(input("How many pennies?:"))
#         cost = 3.0
#         profit += cost
#         total_cash = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
#         if resources["water:"] >= MENU["cappuccino"]["ingredients"]["water"] \
#                 and resources["coffee:"] >= MENU["cappuccino"]["ingredients"]["coffee"] \
#                 and resources["milk:"] >= MENU["cappuccino"]["ingredients"]["milk"]:
#             resources["water:"] -= MENU["cappuccino"]["ingredients"]["water"]
#             resources["milk:"] -= MENU["cappuccino"]["ingredients"]["milk"]
#             resources["coffee:"] -= MENU["cappuccino"]["ingredients"]["coffee"]
#             if total_cash > cost:
#                 print(f"Here is ${round(total_cash - cost, 2)} in change.")
#                 print("Here is your cappuccino Enjoy!")
#             elif total_cash == cost:
#                 print("Here is your cappuccino☕️ Enjoy!")
#             elif total_cash < cost:
#                 print("Sorry that's  not enough money. Money refunded.")
#         else:
#             if resources["water:"] < MENU["cappuccino"]["ingredients"]["water"]:
#                 print("Sorry there is not enough water")
#             elif resources["milk:"] < MENU["cappuccino"]["ingredients"]["milk"]:
#                 print("Sorry there is not enough milk")
#             elif resources["coffee:"] < MENU["cappuccino"]["ingredients"]["coffee"]:
#                 print("Sorry there is not enough coffee")
#
#     elif order == "report":
#         for item in resources:
#             drink.append(item)
#         print(drink[0], resources["water:"], "ml")
#         print(drink[1], resources["milk:"], "ml")
#         print(drink[2], resources["coffee:"], "g")
#         print(f"Money: {profit}")
#
#     elif order == "off":
#         coffee_on = False
# print("Thanks, come back later")
# So this style of programming is called Procedural
# Programming where we set up procedures or functions that do particular things.
# And then one procedure leads to another procedure, and all in all, the computer's
# mostly working from top to bottom and then jumping out into a function as
# needed.
# The end of Procedural Programming


# Day 16 ____Object Oriented Programming (OOP)

# The reason why Object-Oriented Programming is called that is because it's trying to model a real world object.
# The two most important things that make up an object: its attributes and its
# methods.
# **An attribute is just a fancy word for a variable that's associated with a
# modeled object like in our example of a waiter.
# we call it a method because it's a function that a particular modeled
# object can do.
# Those objects have things, and they also can do things,
# the things that they have are their attributes and these are usually modeled with variables,
# and the things that they can do are called methods, and they are modeled by functions.
# So essentially, an object is just a way of combining some piece of data and some
# functionality altogether in the same thing.
# **But we can actually have multiple objects generated from the same type.
# So when we've modeled a particular job in our virtual restaurant
# like the waiter's job, and we figured out what are the things that the waiter have and what are the
# things that it can do, well, we can actually generate multiple versions of the same object. So we could have
# Henry who's a waiter, and we can also have Betty who's a waiter,
# and we can generate as many of these as we want from the same blueprint.
# And in OOP we call this blueprint, or this type, a class.
# And we call these individual objects that are generated from the blueprint an object.

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "c"
# print(table)
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "c"
# print(table)

# Python Turtle Graphics

# Calling the attribute doesn't require '()'
# while calling of functions or methods require such
# Note: A function that is tied to an object is called a method.

import turtle
timmy = turtle.Turtle()
# print(timmy)


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("black", "green")
# my_screen = Screen()
# print(my_screen.canvheight)

# timmy.forward(100)
# timmy.left(90.0)
# timmy.forward(100)
# timmy.left(90.0)
# timmy.forward(100)
# timmy.left(90.0)
# timmy.forward(100)
# for square in range(4):
#     timmy.forward(100)
#     timmy.left(90.0)
#     shorter way of writing the code.

# for dashed_line in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# drawing different shapes
# for _ in range(3):
#     timmy.right(120)
#     timmy.forward(100)
# for _ in range(4):
#     timmy.color('blue')
#     timmy.right(360/4)
#     timmy.forward(100)
# for _ in range(5):
#     timmy.color('green')
#     timmy.right(360/5)
#     timmy.forward(100)
# for _ in range(6):
#     timmy.color('red')
#     timmy.right(360/6)
#     timmy.forward(100)
# for _ in range(7):
#     timmy.color('yellow')
#     timmy.right(360/7)
#     timmy.forward(100)
# for _ in range(8):
#     timmy.color('brown')
#     timmy.right(360/8)
#     timmy.forward(100)
# for _ in range(9):
#     timmy.color('violet')
#     timmy.right(360/9)
#     timmy.forward(100)
# for _ in range(10):
#     timmy.color('blue')
#     timmy.right(360/10)
#     timmy.forward(100)

colours = ["cornflowerBlue", "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtle.colormode(255)


# Here I tapped into the turtle module and set the color mode to 255, because it might not be within that range.

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(50)


# Didn't write this code entirely on my own, took from Angela
def moves():
    movement = [0, 90, 180, 270]
    timmy.forward(30)
    timmy.setheading(random.choice(movement))
    return movement


# In this function I utilized the keyword 'tuple' and it's usage
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return timmy.color(color_tuple)


# is_on = True
# while is_on:
#     timmy.pensize(7)
#     timmy.color(random.choice(colours))
#     random_color()
#     moves()
#     continue
#
# for _ in range(100):
#     random_color()
#     timmy.speed("fastest")
#     timmy.circle(100)
#     timmy.left(7.5)
#     timmy.circle(100)
#
#
# def move_forward():
#     timmy.forward(50)


# my_screen.listen()
#  we have to bind a function that will be triggered when a particular key is
#  pressed on the keyboard.
# my_screen.onkey(key="space", fun=move_forward)
# my_screen.exitonclick()


# Event Listeners.
# Now here's a really important point; when we use a function as an argument,
# something that will be passed into another function,
# we don't actually add the parentheses at the end.
# The parentheses trigger's the function to happen there and then.

# Higher Order Functions.
# And the idea of a higher order function is a function that can work with other functions.
# I recommend that when you're using methods that you haven't created yourself
# like for example onkey, to use keyword arguments
# instead of positional arguments

# STATE:
# Now the fact that each of these objects can have different attributes and can be
# performing different methods at any one time in programming is known as their
# state.


# Class Inheritance
# The process of inheriting behavior and appearance from an existing class is known as class inheritance.

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
#
# class Fish(Animal):
#     # This format here indicates on how to inherit a class from another.
#     def __init__(self):
#         super().__init__()
#
#     # This part of the code, I inherited the function from the super class 'FISH' and modified it.
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#
#     def swim(self):
#         print("moving in water")
#
#
# nemo = Fish()
# nemo.breathe()
# nemo.swim()


#                   FILE HANDLING

# ** How to Open, Read, and Write to Files using the with Keyword **
#
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
#
# file.close()

# or we can choose to follow another approach, which automatically closes the file
# with open("../../Desktop/my_file.txt") as file:
#    This file path here relate to a typical example of a relative file path
#   contents = file.read()
#    print(contents)
# w = write(NB: This overwrites the previous code string)
# r = read
# a = append(To add to the code, unlike 'w')


# with open("C:/Users/hp/Desktop/my_file.txt", mode="a") as file:
#      This file path relate to an absolute file path.
#     file.write(("\nNew text."))
# NB: we use ../ to move up a file directory.


# txt = "I like bananas"
#
# x = txt.replace("bananas", "apples")
#
# print(x)

# txt = "one one was a race horse, two two was one too."
#
# x = txt.replace("one", "three")
#
# print(x)

# txt = "one one was a race horse, two two was one too."
#
# x = txt.replace("one", "three", 2)
#
# print(x)

# txt = "banana"
#
# x = txt.strip()
#
# print("of all fruits", x, "is my favorite")


# txt = ",,,,,rrttgg.....banana....rrr"
#
# x = txt.strip(",.grt")
#
# print(x)
