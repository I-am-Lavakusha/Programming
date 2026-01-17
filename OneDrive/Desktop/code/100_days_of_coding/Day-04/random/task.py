import random
import my_module
#this my_module is created to understand how we can create and use our own module

print(my_module.my_variable)

#random.randint(start, end) it will generate a random number inclusive start and end

random_value=random.randint(10,20)
print(random_value)

#random.random() this will generate a floating value in the range 0 and 1 
#exclusive of 1

random_0_to_1=random.random()
print(round(random_0_to_1, 2))

#random.uniform(start, end) this will generate a random floating number in the range start and end inclusive 

random_float=random.uniform(1,10)
print(random_float)

#this is the program to flip a coin and to check whether the coin is heads or tails if 0-heads else tails

coin=random.randint(0,1)
if coin==0:
    print("heads")
else:
    print("tails")