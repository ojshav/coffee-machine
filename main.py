from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

print("welcome to the office coffee machine")
print("you can choose your drink, see the ingredients by clicking on report and you can turn off the machine by the use"
      "of OFF keyword")
is_on = True
while is_on:

    option = menu.get_items()
    choice = input("What would you like?: ")
    if choice == "OFF":
        is_on = False
    elif choice == "report":
         coffee_maker.report()
         money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





