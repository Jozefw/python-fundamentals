import random
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
rand_num = random.randint(0,len(names)-1);
rando=names[rand_num]
print(f"{rando} is going to buy the meal today!")