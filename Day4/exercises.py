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


#Treasure map
row1 = ["a1", "a2", "a3"]
row2 = ["b1", "b2", "b3"]
row3 = ["c1", "c2", "c3"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")