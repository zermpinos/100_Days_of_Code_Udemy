from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    print('Welcome to the coffee shop!')
    options = menu.get_items()

    print('\nPrice menu!')
    for option in options.split('/'):
        drink = menu.find_drink(option.strip())
        if drink:
            print(f'{drink.name.capitalize()}: ${drink.cost}')

    coffee_selection = input('What would you like? (espresso / latte / cappuccino): \n').lower().strip()

    if coffee_selection == 'off':
        print('Coffee machine is turning off for maintenance. Bye bye!')
        coffee_machine_on = False
    elif coffee_selection == 'report':
        coffee_maker.report()
        money_machine.report()
        input("Press Enter to continue...")
    else:
        drink = menu.find_drink(coffee_selection)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.process_coins()
                payment_successful = money_machine.make_payment(drink.cost)
                if payment_successful:
                    coffee_maker.make_coffee(drink)
            input("Press Enter to continue...")
