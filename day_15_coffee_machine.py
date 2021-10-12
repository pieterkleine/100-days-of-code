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

def coin_input(drink):
    price = MENU[drink]["cost"]
    print(f"The price of a {drink} is ${price}. Please insert coins.")
    # DONE 7. Prompt user to insert coins (if there are enough resources for the drink).
    # DONE 8. Coins are entered by quarter, dime, nickles, pennies and input is calculated.
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters, dimes, nickles, pennies

def calculate_change(drink, quarters, dimes, nickles, pennies):
    coin_total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    # DONE 9. If input is insufficient, return a refund with a message: "Sorry, that's not enough money. Money refunded".
    # DONE 10. If sufficient, add money to the money's resources.
    # DONE 11. Calculate change and return change (2 decimal places).
    if coin_total >= MENU[drink]["cost"]:
        global MONEY
        MONEY += MENU[drink]["cost"]
        if coin_total > MENU[drink]["cost"]:
            change = round(coin_total - MENU[drink]["cost"], 2)
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False

def make_drink(drink):
    # DONE 12. Make coffee: deduct recipe from resources.
    # DONE 13. Wish the customer an enjoyable experience "Here's your x. Enjoy!".
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Here's your {drink} ☕. Enjoy!")

offswitch = "on"
MONEY = 0

while offswitch == "on":
    coffeetype = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
    if coffeetype == "off":
        offswitch = "off"
        break
    elif coffeetype == "report":
        print_report()
    elif coffeetype in MENU:
        if check_resources(coffeetype):
            quarters, dimes, nickles, pennies = coin_input(coffeetype)
            if calculate_change(coffeetype, quarters, dimes, nickles, pennies):
                make_drink(coffeetype)
    else:
        print("Invalid input")