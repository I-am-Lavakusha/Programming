#lists
# this is all about python in built data structure lists
# syntax: fruits=[element1, element2,......element_n]
# lists are ordered
# lists allows duplicates
# lists allows heterogeneous elements
# size is dynamic

states_of_india=["karnataka", "tamilnaadu", "AP", "MP", "Bihaar", "Raajasthan"]
print(states_of_india[0]) #accessing elements by index value
#lists are zero indexed
# python allows negative indexing also

print(states_of_india[-1]) #starts indexing from last
print(states_of_india[-2])

#we can update the lists with indexing
states_of_india[0]="kerala"
states_of_india[-1]="kashmir"

#Now we will see the updated list with kerala and kashmir
print(states_of_india)

#there are so many methods for lists 
#append()
#remove()
#pop()
#extend() etc always go through documentations.