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
money_in_machine = 0.0
money_inserted = 0.0
###########################

def insert_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickels = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))

    return quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01


def enough_resources(choice):
    enough_resources = True

    if resources['water'] < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        enough_resources = False
    
    if resources['coffee'] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        enough_resources = False
    
    if 'milk' in MENU[choice]["ingredients"]:
        if resources['milk'] < MENU[choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            enough_resources = False
    
    return enough_resources


def coffee_dispensed(choice):
    resources['water'] -= MENU[choice]["ingredients"]["water"]
    resources['coffee'] -= MENU[choice]["ingredients"]["coffee"]
    if 'milk' in MENU[choice]["ingredients"]:
        resources['milk'] -= MENU[choice]["ingredients"]["milk"]
    change = money_inserted - MENU[choice]["cost"]

    print(f"Here is ${change:.2f} in change.")
    print(f"Here is your {choice}. Enjoy!")


def coffee_machine(): 
    global resources
    global money_in_machine
    global money_inserted


    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while choice not in ["espresso", "latte", "cappuccino", "report", "off", "replenish"]:
        choice = input("Invalid choice. Enter what you would like: ").lower()
    
    if choice == 'off':
        print("Thank you!")
        return
    
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_in_machine}")
    
    elif choice == 'replenish':
        resources['water'] += int(input("Water Added in ml: "))
        resources['milk'] += int(input("Milk Added in ml: "))
        resources['coffee'] += int(input("Coffee Added in g: "))
    
    else:
        

        if enough_resources(choice):

            money_inserted = insert_money()

            if money_inserted < MENU[choice]["cost"]:
                print(f"Sorry, that's not enough money. ${money_inserted} refunded.")

            else:
                coffee_dispensed(choice)
                money_in_machine += MENU[choice]["cost"]
        
    coffee_machine()

coffee_machine()