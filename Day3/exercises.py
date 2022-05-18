#if-else statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


#Odd or even / modulo operator
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


#Nested if-else statemtent
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")


#bmi
weight = int(input("What is your weight in kg? "))
height = float(input("What is your height in m? "))
bmi = round(weight / height ** 2 , 1)
print(f"Your bmi is {bmi}.")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")


#leap-year problem
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


#Multiple if statemtents
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
    
else:
    print("Sorry, you have to grow taller before you can ride.")


#Pizza order practice 
greeting = "Welcome to Python Pizza Deliveries!"
print(greeting)

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")


#Love calculator
greeting = "Welcome to the Love Calculator!"
print(greeting)
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_name = (name1 + name2).lower()

t = combined_name.count("t") 
r = combined_name.count("r") 
u = combined_name.count("u") 
e = combined_name.count("e") 
true = t + r + u + e

l = combined_name.count("l") 
o = combined_name.count("o") 
v = combined_name.count("v") 
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")