#Mohit_Maurya: 11/01/2021
#Coffee Machine Program
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

money = 0


def report(resources, money):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


def remain_res(MENU, resources, coffee_type):
    remain = {}
    remain["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
    if coffee_type == "espresso":
        remain["milk"] = resources["milk"]
    else:
        remain["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
    remain["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
    return remain


def check_res(MENU, resources, coffee_type):
    remain = remain_res(MENU, resources, coffee_type)
    for i in remain:
        if remain[i] < 0:
            print(f"Sorry there is not enough {i}.")
            return True
        else:
            return False


def money_paid():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    paid = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return paid


while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_type == "off" or coffee_type == "report" or coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        if coffee_type == "off":
            break

        if coffee_type == "report":
            report(resources, money)
            continue

        if check_res(MENU, resources, coffee_type):
            continue

        change = money_paid() - MENU[coffee_type]["cost"]
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif change > 0:
            print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {coffee_type} ☕ Enjoy!")
        resources = remain_res(MENU, resources, coffee_type)
        money += MENU[coffee_type]["cost"]
    else:
        print("Invalid request! Please enter your request again.")
