# # Pretty Table in PyPi
# from prettytable import *

# pokemon_table = PrettyTable()



# pokemon_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# pokemon_table.add_column("Type", ["Electric", "Water", "Fire"])

# pokemon_table.align="l"

# print(pokemon_table)


class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    

class Menu:
    def __init__(self) -> None:
        self.menu_list = [
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24),
        ]
    
    def get_items(self) -> str:
        return '/'.join([item.name for item in self.menu_list])
    
    def find_drink(self, order_name):
        for item in self.menu_list:
            if item.name == order_name:
                return item
        return None


class CoffeeMaker:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:  
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def make_coffee(self, order: MenuItem):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def add_resources(self, water, milk, coffee):
        self.resources['water'] += water
        self.resources['milk'] += milk
        self.resources['coffee'] += coffee

class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self) -> None:
        self.money_received = 0.0
        self.profit = 0.0
    
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
    
#Driver Code

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "replenish":
        water = int(input("Water Added in ml: "))
        milk = int(input("Milk Added in ml: "))
        coffee = int(input("Coffee Added in g: "))

        coffee_maker.add_resources(water, milk, coffee)

    elif menu.find_drink(choice)!= None:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
    else:
        print("Wrong choice entered.")