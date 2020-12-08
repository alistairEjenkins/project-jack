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
money = 0.0

def make_coffee(choice):

    for ingredient, amount in MENU[choice]['ingredients'].items():
        resources[ingredient] -= amount
    print(f'Here is your {choice}. Enjoy!')


def transaction_successful(amount_entered, cost):
    global money

    if amount_entered < cost:
        print('Insufficient funds')
        return False
    elif amount_entered == cost:
        money += cost
        return True
    else:
        print(f'Here is your ${round(amount_entered - cost,2)} change')
        money += cost
        return True

def process_coins():
    coins = {'quarter': 0.25, 'dime': 0.10, 'nickel': 0.05, 'penny': 0.01, }
    total = 0.0
    print('Please insert coins')
    for coin, value in coins.items():
        total += float(input(f'How many {coin}s? ')) * value
    return total


def sufficient_resources(choice):
    for ingredient, amount in MENU[choice]['ingredients'].items():
        if (resources[ingredient] - amount) < 0:
            print(f'insufficient {ingredient}. Sorry.')
            return False
    return True


def print_resources():
    print('Resources')
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f'Money : ${money}')


coffee_machine_on = True
while coffee_machine_on:
    #TODO : Prompt user
    print("What would you like (espresso/latte/cappuccino)? ")
    choice = input('> ')
    #TODO : turn off coffee machine by entering 'off' to the prompt
    if choice.lower() == 'off':
        print('Switching off ...')
        coffee_machine_on = False
    #TODO : print report
    elif choice.lower() == 'print':
        print_resources()
    else:
        #TODO : check sufficent resources
        if sufficient_resources(choice):
            # TODO : Process coins
            total_money_entered = process_coins()
        else:
            print('Please select an alternative.')
            continue
        #TODO : Check transaction successful
        if transaction_successful(total_money_entered, MENU[choice]['cost']):
            # TODO : Make Coffee
            make_coffee(choice)
