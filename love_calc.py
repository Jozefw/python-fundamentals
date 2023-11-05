
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

names = name1 + name2
combined_names = names.lower()
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_num = t+r+u+e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
sec_num =l+o+v+e

total = int(str(first_num) + str(sec_num))
if (total < 10) or (total >90):
  print(f"Your score is {total}, you go together well")
elif (total >= 40) and (total <=50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")