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

# TODO 1. Prompt user which coffee they would like (espresso, latte, cappuccino)
# TODO 2. Check input and continue
# TODO 3. Repeat prompt once the program is terminated
# TODO 4. Turn off the coffee machine whenever "off" is inputed.
# TODO 6. When drink is chosen, check whether resources are suffcient to make drink. Otherwise return Sorry there is not enough x
# TODO 7. Prompt user to insert coins (if there are enough resources for the drink).
# TODO 8. Coins are entered by quarter, dime, nickles, pennies and input is calculated.
# TODO 9. If input is insufficient, return a refund with a message: "Sorry, that's not enough money. Money refunded".
# TODO 10. If sufficient, add money to the money's resources.
# TODO 11. Calculate change and return change (2 decimal places).
# TODO 12. Make coffee: deduct recipe from resources.
# TODO 13. Wish the customer an enjoyable experience "Here's your x. Enjoy!".


def print_report():
    # TODO 5. Print report when user enters "report", which shows the coffee's resource values and money.

offswitch = "on"

while offswitch == "on":
    coffeetype = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
    if coffeetype == "off":
        offswitch = "off"
        break
    elif coffeetype == "report":
        print_report()