#this is just a small program to select a random persom from a group of people to pay the bill
#for this i am going to use the random module
# There are two ways 

import random
friends=["sharath", "swathi", "swapna", "dhanush", "raghu", "rajendra"]

#1 using the choice from random module
#random.choice(seq)  --> this will take the input as a sequence and get a random one
print(random.choice(friends))

#2 
#in this we can use the indexing and the random.randint(start, end) method
random_index=random.randint(0, len(friends)-1)
print(friends[random_index])
print(friends[random.randint(0, len(friends)-1)])
