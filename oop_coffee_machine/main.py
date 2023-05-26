from cgi import print_directory
from unicodedata import name
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
def cls(): #for clearing out console
    os.system('cls' if os.name=='nt' else 'clear')

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

menu = Menu()
machine = CoffeeMaker()
cashier = MoneyMachine()

cls()
while True:
    print("============================================")
    print("Welcome to tlhylmm's tasty coffee machine!")
    print("============================================")
    print("(Use numbers to navigate)\n")
    print("1) Buy coffee")
    print("2) See stock")
    print("3) Turn off")

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
        
        if coffee_type == "1": coffee_type = espresso
        elif coffee_type == "2": coffee_type = latte
        else: coffee_type = cappuccino

        if machine.is_resource_sufficient(coffee_type):
            print(f"That will be ${coffee_type.cost}.")
            if cashier.make_payment(coffee_type.cost):
                machine.make_coffee(coffee_type)                
                input("\nPress any key to return back to main menu.")
                cls()
            else:
                input("\nPress any key to return back to main menu.")
                cls()
        else:
            input("\nPress any key to return back to main menu.")
            cls()
    
    elif navigate == "2":
        cls()
        print("======================")
        print("        STOCK         ")
        print("======================")
        machine.report()
        input("\nPress any key to return back to main menu.")
        cls()
    else:
        quit()