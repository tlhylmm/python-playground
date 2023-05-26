from inspect import walktree
import os
def cls(): #for clearing out console
    os.system('cls' if os.name=='nt' else 'clear')

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
    "money": 0
}


def report():    
    """Reports all the ingredients that left in the machine"""

    print("======================")
    print("        STOCK         ")
    print("======================")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check(coffeetype, insufficient):
    """Check's if there is enough ingredient for given coffee type. Fill's a
       list with insufficient ingredients and returns False if there is any."""

    flag = False #turn True if there are any low ingredients
    for key in MENU[coffeetype]["ingredients"]:
        if MENU[coffeetype]["ingredients"][key] > resources[key]:
            insufficient.append(key)
            flag = True
    if flag:
        return False
    return True

def pay(coffeetype):
    cost = MENU[coffeetype.lower()]['cost']
    total = 0
    print(f"{coffeetype} will cost ${cost}")
    print("Please insert coins.")
    while total < cost:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total += ( (quarters * 0.25) + (dimes * 0.1) +
                (nickels * 0.05) + (pennies * 0.01) )
        total = float("{:.2f}".format(total))
        if total < cost:
            x = cost - total
            x = float("{:.2f}".format(x))
            print(f"You still need ${x}. Please insert coins.")
        elif total > cost:
            x = total - cost
            x = float("{:.2f}".format(x))
            print(f"Here is ${x} in change.")
    resources["money"] += cost

def make_coffee(coffeetype):
    """Just makes coffee. Doesn't check if there are enough ingredients.
       Use check() function to check the stock."""

    for key in MENU[coffeetype.lower()]["ingredients"]:
        resources[key] -= MENU[coffeetype.lower()]["ingredients"][key]

    print(f"\nHere is your {coffeetype}. Enjoy!")
    input("\nPress any key to return back to main menu.")

def fill():
    print("======================")
    print("      FILL STOCK      ")
    print("======================")
    print("Please add your ingredients.")
    water = int(input("How much water in ml?: "))
    milk = int(input("How much milk in ml?: "))
    coffee = int(input("How much milk in grams?: "))
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee
    print("Added to stock.")
    input("\nPress any key to return back to main menu.")


cls()
while True:
    print("============================================")
    print("Welcome to tlhylmm's tasty coffee machine!")
    print("============================================")
    print("(Use numbers to navigate)\n")
    print("1) Buy coffee")
    print("2) See stock")
    print("3) Fill stock")
    print("4) Turn off")

    navigate = input("\nWhat would you like to do?: ")

    while not(navigate == "1" or navigate == "2" or navigate == "3"):
        print("Wrong input. Try again.")
        navigate = input("What would you like to do?: ")
    
    if navigate == "1":
        cls()
        print("======================")
        print("      BUY COFFEE      ")
        print("======================")
        print("(Use numbers to navigate)\n")
        print("1) Espresso")
        print("2) Latte")
        print("3) Cappuccino")

        coffee_type = input("\nWhat type of coffee would you like?: ")
        while not(coffee_type == "1" or
                  coffee_type == "2" or coffee_type == "3"):
            print("Wrong input. Try again.")
            coffee_type = input("What type of coffee would you like?: ")
        
        if coffee_type == "1": coffee_type = "Espresso"
        elif coffee_type == "2": coffee_type = "Latte"
        else: coffee_type = "Cappuccino"

        low_ingredients = []
        if not check(coffee_type.lower(), low_ingredients):
            print(f"\nSorry, ingredients are not enough for {coffee_type}.")
            print("You need ", end = "")
            for item in low_ingredients: print(item, end = "/")
            input("\nPress any key to return back to main menu.")
            cls()
        else:
            print()
            pay(coffee_type)
            make_coffee(coffee_type)
            cls()
    elif navigate == "2":
        cls()
        report()
        input("\nPress any key to return back to main menu.")
        cls()
    elif navigate == "3":
        cls()
        fill()
        cls()
    else:
        quit()

