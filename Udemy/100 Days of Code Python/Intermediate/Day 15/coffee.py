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
on = True

def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    return print(f'Water: {water} ml,\nMilk: {milk} ml,\nCoffee: {coffee},\nMoney: {money} ')


def new_drink(drink):
    valid = 0
    missing = []
    for drinks in MENU:
        if drink == drinks:
            for need in drinks['ingredients']:
                if resources[need] < drinks['ingredients'][need]:
                    valid += 1
                    missing.append[need]
    return valid, missing

def payment(quarters, dimes, nickels, pennies, drink):
    pay = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    success = []
    if pay == MENU[drink]['cost']:
        resources['money'] += pay
        success.append('True')
        return success
    elif pay > MENU[drink]['cost']:
        change = round(pay - MENU[drink]['cost'], 2)
        resources['money'] += MENU[drink]['cost']
        success.append('True')
        success.append(change)
        return success
    elif pay < MENU[drink]['cost']:
        change = pay
        success.append('False')
        success.append(change)
        return success

def refill():
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
    return resources



# if drink == 'espresso':
#     if resources['water'] >= MENU[drink]['ingredients']['water']:
    #         resources['water'] -= MENU[drink]['ingredients']['water']
    #         if resources['coffee'] >= MENU[drink]['ingredients']['coffee']:
    #             resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    #         elif resources['coffee'] < MENU[drink]['ingredients']['coffee']:
    #             return print('Insufficient coffee')
    #     elif resources['water'] < MENU[drink]['ingredients']['water']:
    #         return print('Insufficient water')


while on:
    option = input('What would you like? (espresso/latte/cappuccino): ')
    if option == 'report':
        report()
    elif option == 'refill':
        refill()
    elif option == 'off':
        on = False
    elif option != 'espresso' and option != 'cappuccino' and option != 'latte':
        print('You did not select a valid option')
    elif option == 'espresso' or option == 'cappuccino' or option == 'latte':
        valid = 0
        missing = []
        for drinks in MENU:
            if option == drinks:
                for need in MENU[option]['ingredients']:
                    if resources[need] < MENU[option]['ingredients'][need]:
                        valid += 1
                        missing.append[need]
        if valid == 0 and missing == []:
            for drinks in MENU:
                if option == drinks:
                    quarters = int(input('How many quarters? '))
                    dimes = int(input('How many dimes? '))
                    nickels = int(input('How many nickels? '))
                    pennies = int(input('How many pennies? '))
                    pay = payment(quarters, dimes, nickels, pennies, option)
                    if pay[0] == 'True':
                        for need in MENU[option]['ingredients']:
                            if resources[need] >= MENU[option]['ingredients'][need]:
                                resources[need] -= MENU[option]['ingredients'][need]
                        if pay[1]:
                            print(f'Your change is {pay[1]}. Here is your {option}.')
                    elif pay[0] == 'False':
                        print(f"Your payment of ${pay[1]} does not cover the cost of {option} at ${MENU[option]['cost']}")
        elif valid != 0:
            for item in missing:
                print(f'Sorry the machine is low on {item}.')
    


