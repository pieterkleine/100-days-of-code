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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# DONE 1. Prompt user which coffee they would like (espresso, latte, cappuccino)
# DONE 2. Check input and continue
# DONE 3. Repeat prompt once the program is terminated
# DONE 4. Turn off the coffee machine whenever "off" is inputed.


def print_report():
    # DONE 5. Print report when user enters "report", which shows repothe coffee's resource values and money.
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    print(f"Water: {water_amount}ml\nMilk: {milk_amount}ml\nCoffee: {coffee_amount}g\nMoney: ${money}")

def check_resources(drink):
    # TODO 6. When drink is chosen, check whether resources are suffcient to make drink. Otherwise return Sorry there is not enough x
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
    elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        return True

def coin_input():
    # TODO 7. Prompt user to insert coins (if there are enough resources for the drink).
    # TODO 8. Coins are entered by quarter, dime, nickles, pennies and input is calculated.
    return

def calculate_change(quarters, dimes, nickles, pennies):
    # TODO 9. If input is insufficient, return a refund with a message: "Sorry, that's not enough money. Money refunded".
    # TODO 10. If sufficient, add money to the money's resources.
    # TODO 11. Calculate change and return change (2 decimal places).
    return

def make_drink(drink):
    # TODO 12. Make coffee: deduct recipe from resources.
    # TODO 13. Wish the customer an enjoyable experience "Here's your x. Enjoy!".
    return  

offswitch = "on"
money = 0

while offswitch == "on":
    coffeetype = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
    if coffeetype == "off":
        offswitch = "off"
        break
    elif coffeetype == "report":
        print_report()
    elif coffeetype in MENU:
        if check_resources(coffeetype):
            print("Ok")
        coin_input()
        calculate_change(quarters, dimes, nickles, pennies)
        make_drink(coffeetype)
    else:
        print("Invalid input")