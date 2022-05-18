import random

#Heads or tails
flip = random.randint(0, 1)
if flip == 0:
    coin = "Tails"
elif flip == 1:
    coin = "Heads"
print(coin)


#Banker roulette
names = input("\nGive me everybody's name, seperated by comma. ")
name_list = names.split(",")
message = "is going to buy the meal today."
##option 1
person_who_will_pay = random.choice(name_list).title()
print(f"{person_who_will_pay} {message} ")
##optioin 2
person_who_will_pay = name_list[random.randint(0, len(name_list)-1)].title()
print(f"{person_who_will_pay} {message}")


#