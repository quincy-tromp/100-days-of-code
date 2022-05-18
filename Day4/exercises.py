import random

#Heads or tails
flip = random.randint(0, 1)
if flip == 0:
    coin = "Tails"
elif flip == 1:
    coin = "Heads"
print(coin)


#Banker roulette
names = input("Give me everybody's name, seperated by comma. ")
name_list = names.split(",")
message = "is going to buy the meal today."
##option 1
person_who_will_pay = random.choice(name_list).title()
print(f"{person_who_will_pay} {message} ")
##optioin 2
person_who_will_pay = name_list[random.randint(0, len(name_list)-1)].title()
print(f"{person_who_will_pay} {message}")


#Treasure map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?" + " " + 
"(For example column 2, row 3 would be entered as: 23) ")
column = int(position[0])
row = int(position[1])
map[row-1][column-1] = "💰"

print(f"{row1}\n{row2}\n{row3}")