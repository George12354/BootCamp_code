from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
main_menu = Menu()
coin_processor = MoneyMachine()

while is_on:
    choice = input(f"What would you like? ({main_menu.get_items()}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        coin_processor.report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'capuccino':
        chosen_drink = main_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(chosen_drink) and coin_processor.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)
