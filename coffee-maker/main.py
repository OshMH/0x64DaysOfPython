from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine






def main():
    menu1 = Menu()
    coffeeMaker1 = CoffeeMaker()
    moneyMachine1 = MoneyMachine()
    turnOff:bool = False
    while(not turnOff):
        order = input(f"What drink do you want from these?: {menu1.get_items()}")
        if order == "off":
            print("Turning machine off thanks")
            turnOff = True
            break
        if order == "report":
            coffeeMaker1.report()
        orderedDrink = menu1.find_drink(order)
        if coffeeMaker1.is_resource_sufficient(orderedDrink):
            if moneyMachine1.make_payment(orderedDrink.cost):
                coffeeMaker1.make_coffee(orderedDrink)
            

    
    

if __name__ == "__main__":
    main()