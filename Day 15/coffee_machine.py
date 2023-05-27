
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

resources = {'water': 300, "milk": 200, "coffee": 100, 'money': 0}

coffee_machine_on = True

while coffee_machine_on:
    print('Welcome to the coffee shop!')
    print('\nPrice menu!\nEspresso: $1.5\nLatte: $2.5\nCappuccino: $3.0\n')
    coffee_selection = input('What would you like? (espresso / latte / cappuccino): \n').lower().strip()

    if coffee_selection == 'off':
        print('Coffee machine is turning off for maintenance. Bye bye!')
        coffee_machine_on = False
    elif coffee_selection == 'report':
        for item, quantity in resources.items():
            if item == 'water':
                print(f'Water: {quantity}ml')
            elif item == 'milk':
                print(f'Milk: {quantity}ml')
            elif item == 'coffee':
                print(f'Coffee: {quantity}g')
            elif item == 'money':
                print(f'Money: ${quantity:.2f}')
        input("Press Enter to continue...")
    else:
        drink = MENU.get(coffee_selection)
        if drink:
            ingredients = drink['ingredients']
            cost = drink['cost']
            insufficient_resources = False

            for ingredient, quantity in ingredients.items():
                if resources[ingredient] < quantity:
                    print(f"Sorry, there is not enough {ingredient}.")
                    insufficient_resources = True

            if insufficient_resources:
                input("Press Enter to continue...")
                continue

            quarters = int(input('How many quarters are you inserting? \n'))
            dimes = int(input('How many dimes are you inserting? \n'))
            nickels = int(input('How many nickels are you inserting? \n'))
            pennies = int(input('How many pennies are you inserting? \n'))
            coins_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

            if coins_inserted < cost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(coins_inserted - cost, 2)
                resources['money'] += cost
                for ingredient, quantity in ingredients.items():
                    resources[ingredient] -= quantity
                print(f"Here is your {coffee_selection}☕. Enjoy!")
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")

            input("Press Enter to continue...")
        else:
            print("Invalid selection. Please choose from the available options.")
            input("Press Enter to continue...")
