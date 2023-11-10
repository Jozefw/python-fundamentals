import random

random_int = random.randint(1,10)
print(random_int)

rand_float = random.random() * 5
print(rand_float)

import random

side = random.randint(0,1)

if side == 0:
  print("Tails")
else:
  print("Heads")
