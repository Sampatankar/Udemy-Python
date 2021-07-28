# Set Resources and costs:
# Resource costs per choice:
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

# Starting machine resources:
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
money = 0

# FUNCTIONS:
# Resource report:
def print_report(resources, money):
    print([key for key in resources.keys()][0].title() + ": " + str([value for value in resources.values()][0]) + "ml")
    print([key for key in resources.keys()][1].title() + ": " + str([value for value in resources.values()][1]) + "ml")
    print([key for key in resources.keys()][2].title() + ": " + str([value for value in resources.values()][2]) + "g")
    print(f"Money: £{money}")

print_report(resources, money)


# Calculate change:
def calculate_change(total_quarters, total_dimes, total_nickels, total_pennies, cost):

    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    quarters = total_quarters * quarter
    dimes = total_dimes * dime
    nickels = total_nickels * nickel
    pennies = total_pennies * penny
    total_money = quarters + dimes + nickels + pennies

    change = (total_money - cost)

    return change


"""
BUILD OUT COFFEE MACHINE!!!
1. On/Off switch
2. Report function
3. Loop through to choose coffee order,
4. or, report resource deficit:
    - not enough cash - refund cash and say no coffee
    - not enough resources - choose another thing
        - money taken last...as may not have enough resource. 
"""
