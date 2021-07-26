"""
KEY POINTS:
1. 3 hot flavours
2. coins operated
    - Penny - 1 cent, Dime - 10 cents, Nickel - 5 cents, Quarter - 25 cents
3. automatic cup dispenser
4. counting cup selling

Analytic table:
- water inlet
- coin slot
- coin acceptor
- LCD display
- Drink 1, 2 or 3
+ or -
- Menu
- Drink Outlet
- Waster water box

PROGRAM SPEC:
1. Print Report
2. Check Resources Sufficient
3. Process coins
4. Check transaction successful
5. Make Coffee
"""
# TODO: 1. Print a report of all coffee machine resources
# TODO: 2. Check resources sufficient to make drink order

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

Money = 0
# What do they want to order?
order = input("What would you like? (espresso/latte/cappuccino): ")


# Print the resource report:
def print_report(resources, Money):
    print([key for key in resources.keys()][0].title() + ": " + str([value for value in resources.values()][0]) + "ml")
    print([key for key in resources.keys()][1].title() + ": " + str([value for value in resources.values()][1]) + "ml")
    print([key for key in resources.keys()][2].title() + ": " + str([value for value in resources.values()][2]) + "g")
    print(f"Money: £{Money}")


# If 'report' requested:
if order == "report":
    print_report(resources, Money)


# Total coins and change calculator:
