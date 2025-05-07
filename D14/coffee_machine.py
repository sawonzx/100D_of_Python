from Data import MENU, resources

def print_report():
    """Show Available Resources"""
    global balance
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${balance}"


#4
def check_resources(coffee_name):
    """Check resources sufficient?"""
    for ingredient in MENU[coffee_name]["ingredients"]:
        if resources[ingredient] < MENU[coffee_name]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


#5 & 6
def process_coin(coffee_name):
    """Take input and Make a transaction"""
    global balance
    user_paid = 0.00
    print("Please insert coins.")
    user_paid += float(input("How many quarters: ")) * 0.25
    user_paid += float(input("How many dimes: ")) * 0.1
    user_paid += float(input("How many nickel: ")) * 0.05
    user_paid += float(input("How many pennies: ")) * 0.01

    if MENU[coffee_name]["cost"] > user_paid:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        balance += MENU[coffee_name]["cost"]
        user_paid -= MENU[coffee_name]["cost"]
        print(f"Here is {user_paid:.2f} dollars in change.")
        return True
    

#7
def make_coffee(coffee_name):
    """Rewrite the available resources after making a Coffee"""
    for ingredient in MENU[coffee_name]["ingredients"]:
        resources[ingredient] -= MENU[coffee_name]["ingredients"][ingredient]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


def coffe_machine_main():
    global switch
    while switch:
        #1
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # 2
        if user_input == "off":
            switch = False

        # 3
        elif user_input == "report":
            print(print_report())

        elif user_input == "espresso" or "latte" or "cappuccino":
            if check_resources(user_input):
                if process_coin(user_input):
                    make_coffee(user_input)


balance = 0.00
switch = True
coffe_machine_main()
