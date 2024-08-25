from Treasure_island_ASCII import island, doors, fire_game_over, win, treasure

print(treasure)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

user_input = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if user_input == 'left':
    print(island)
    user_input = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait '
                       'for a boat. Type "swim" to swim across.\n')
else:
    print("You fell into a hole. Game Over.")

if user_input == "wait":
    print(doors)
    user_input = input(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which "
        "colour do you choose?\n")
else:
    print("You get attacked by an angry trout. Game Over.")

if user_input == "yellow":
    print(fire_game_over)
    print("It's a room full of fire. Game Over.")
elif user_input == "blue":
    print("You found the treasure! You Win!")
elif user_input == "red":
    print(fire_game_over)
    print("You enter a room of beasts. Game Over.")
else:
    print(win)
    print("You chose a door that doesn't exist. Game Over.")
