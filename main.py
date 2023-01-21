from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffemaker = CoffeeMaker()

menu = Menu()

print(f"The following items are available: {menu.get_items()}")
is_on = True
while is_on:
    choice = input("What would you like to drink? ")
    if choice == "report":
        coffemaker.report()
        moneymachine.report()
    elif choice == "off":
        is_on = False
    else:
        menu.find_drink(choice)
        if moneymachine.make_payment(menu.find_drink(choice).cost):
            if coffemaker.is_resource_sufficient(menu.find_drink(choice)):
                coffemaker.make_coffee(menu.find_drink(choice))

