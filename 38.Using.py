import random

a = random.random() # it generates 0 - 1.0
print(a)

rand_int = random.randint(1,10) # Prints int from [1,10]
print(rand_int)

name_list = ['one','two','three','four','five']
print (random.choice(name_list)) # Choose random from list
