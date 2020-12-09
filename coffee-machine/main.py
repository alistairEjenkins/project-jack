from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    cm = CoffeeMaker()
    m = Menu()
    mm = MoneyMachine()
    print(f'What would you like to order please {m.get_items()}')
    choice = m.find_drink(input('> '))
    if cm.is_resource_sufficient and mm.make_payment(choice.cost):
        cm.make_coffee(choice)
    if (input('Report? ')) == 'y':
        cm.report()
        mm.report()

if __name__ == '__main__':
    main()