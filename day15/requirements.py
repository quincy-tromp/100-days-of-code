#REQUIREMENTS
#------------------

# Makes 3 hot flavours - Espresso, Latte, and Cappuccino.
# Espresso ($1.50): 50ml water, 18g coffee
# Latte ($2.50): 200ml water, 24g coffee, 150ml milk
# Cappuccino ($3.00): 250ml water, 24g coffee, 100ml milk

# The coffee machine has some resources that it has to manage. It starts out with 300ml water, 200ml milk, 100g coffee

# Coin operated: Penny (1 cent), Nickel (5 cents), Dime (10 cents), Quarter (25 cents)

#--1
# Needs to be able to print a report. To tell us what resources it has left (how much water, milk, coffee).

# Starts off with the prompt -> 'What would you like? (espresso/latte/cappuccino): ' 
# If you input 'report', it will return a report with how much water, milk, coffee, money it has left -
    # 'Water: 300ml'
    # 'Milk: 200ml'
    # 'Coffee: 100g'
    # 'Money: $0' 
# Then it comes back to the prompt.

#--2
# Needs to be able to check if the resources are sufficient when a user orders a drink.

# When you input one of the 3 options at the prompt, it will tell you to insert coins - 'Please insert coins.'
# Then it will ask how many quarteres, dimes, nickels, and pennies?: 
# Then it will give you (display) your change - 'Here is $2.42 in change.'
# Then it will give you (display) your order - 'Here is your latte  *emoji* Enjoy!'
# Returns to the prompt 

# If there isn't sufficient resources, it will tell you what resource is not enough -
# 'Sorry, there is not enough water.'

#--3
# Needs to be able to process coins.

# When you order something it will ask you, one for one for each coin, how many you'll insert - 

# If you don't insert enough, it will tell you - 'Sorry, that's not enough money. Money refunded.'

#--4 
# Needs to able to check if transaction was successful.

#--5
# Make coffee.

# Update resource quantity.

#--6 
# Turn off the Coffee Machine by entering 'off' to the prompt.
