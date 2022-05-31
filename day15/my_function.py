from ascii_art import logo
from resources_data import MENU


def take_order():
    ''' 
    Displays the logo and menu, takes the customer's order, and then returns the customer's order in lowercase.
    -------
    Returns
        customer_order (str): customer's order
    '''
    print(logo)
    for item in MENU:
        print(f"{item.title()}: $", "{:.2f}".format(MENU[item]['cost']))
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice


def report(inventory):
    '''
    Takes the inventory and displays the quantity of each resource, right-aligned.
    ------
    Args
        inventory (list): list with variables that hold the quantity of each resource
    '''
    print(f"Water: {inventory['water']: > 5}")
    print(f"Milk: {inventory['milk'] : > 6}")
    print(f"Coffee: {inventory['coffee'] : > 4}")
    print("Money: ${:<.2f}".format(inventory['money']))


def check_resources(customer_order, inventory):
    '''
    Takes the customer's order and the current inventory, checks if there's enough inventory,
    and returns result, if there are sufficient resources or not.
    --------
    Args
        customer_order (str): in lowercase - latte, espresso, or cappuccino 
        inventory (list): list with variables that hold the quantity of each resource
    Returns
        sufficient_resources (bool): result of the check; True or False
    '''
    sufficient_resources = False

    water_needed = MENU[customer_order]['ingredients'].get('water', 0)
    milk_needed = MENU[customer_order]['ingredients'].get('milk', 0)
    coffee_needed = MENU[customer_order]['ingredients'].get('coffee', 0)
   
    if ((inventory['water'] >= water_needed) and
        (inventory['milk'] >= milk_needed) and
        (inventory['coffee'] >= coffee_needed)):
        sufficient_resources = True

    return sufficient_resources


def not_sufficient_resources(customer_order, inventory):
    '''
    Takes the customer's order and the current inventory, when there's not enough inventory,
    and displays the resource that there is not enough of.
     --------
    Args
        customer_order (str): in lowercase - latte, espresso, or cappuccino 
        inventory (list): list with variables that hold the quantity of each resource
    '''
    water_needed = MENU[customer_order]['ingredients'].get('water', 0)
    milk_needed = MENU[customer_order]['ingredients'].get('milk', 0)
    coffee_needed = MENU[customer_order]['ingredients'].get('coffee', 0)
    
    if inventory['water'] < water_needed:
        print("Sorry, there is not enough water.")
    if inventory['milk'] < milk_needed:
        print("Sorry, there is not enough milk.")
    if inventory['coffee'] < coffee_needed:
        print("Sorry, there is not enough coffee.")


def process_coins(customer_order):
    '''
    Takes the customer's order, gathers the cost data, calculates the sum of the money received from the customer, 
    checks if it's enough. If the money received is not enough, the money is refunded. Else the money is processed 
    and the change is calculated, if applicable. Returns the money amount processed.
    ---------
    Args
        customer_order (str): the customer's order
    Returns
        payment (float): the total money processed, with a 2 point precision
    '''
    print("Please insert coins.")

    drink_cost = MENU[customer_order]['cost']

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    money_received = ((quarters * 0.25) +
            (dimes * 0.10) +
            (nickels * 0.05) + 
            (pennies * 0.01))
    
    if money_received < drink_cost:
        payment = 0
    elif money_received > drink_cost:
        change = money_received - drink_cost
        payment = money_received - change
        print("Here is ${:.2f} in change.".format(change))
    else:
        payment = money_received

    return float(payment)


def transact(payment):
    '''
    Takes the amount of money processed by the machine and returns if the transaction was successful or not.
    -----
    Args
        payment (float): the total money processed, with a 2 point precision
    '''
    transaction_successful = False
    if payment > 0:
        transaction_successful = True
        
    return transaction_successful


def make_order(customer_order):
    '''
    Displays order made.
    '''
    print(f"Here is your {customer_order} ☕ Enjoy!")


def update_resource_quantities(customer_order, payment, inventory):
    '''
    Takes the customer's order, the money amount processed by the machine, and the inventory, 
    and updates the current inventory for all resources.
    ----
    Args
        customer_order (str): the customer's order
        payment (float): the total money processed, with a 2 point precision
        inventory (list): list with variables that hold the quantity of each resource
    '''
    water_needed = MENU[customer_order]['ingredients'].get('water', 0)
    milk_needed = MENU[customer_order]['ingredients'].get('milk', 0)
    coffee_needed = MENU[customer_order]['ingredients'].get('coffee', 0)
    inventory['water'] -= water_needed
    inventory['milk'] -= milk_needed
    inventory['coffee'] -= coffee_needed
    inventory['money'] += payment