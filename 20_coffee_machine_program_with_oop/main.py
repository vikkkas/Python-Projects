from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_input = input("What would you like to have? latte/cappuccino/espresso:").lower()
    if user_input == "off":
        is_on=False
    elif user_input=="report":
        money_machine.report()
        coffee_maker.report()
    else:           
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)