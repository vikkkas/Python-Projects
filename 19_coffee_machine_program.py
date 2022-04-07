MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredient):
    """Returns True if order can be made, False if ingredients are insufficent"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            return True
        
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert Coins")
    total = int(input("How many quarters ?:")) * 0.25
    total+= int(input("How many dimes ?:")) * 0.1
    total+= int(input("How many nickles ?:")) * 0.05
    total+= int(input("How many pennies ?:")) * 0.01
    return total

def is_transaction_successfull(money_received,drink_cost):
    """Returns true when the payment is accepted, or false when if the money is insufficent"""
    if money_received>=drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here's is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resource"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here's your {drink_name} ☕🍵")

machine_on = True

while machine_on:
    user_input=input("What would you like?(espresso/latte/cappuccino):").lower()
    if user_input == "off":
        machine_on=False
    elif user_input=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(user_input,drink["ingredients"])