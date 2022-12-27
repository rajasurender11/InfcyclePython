#int float string bool
#list (changable)
#tuple( not  changable)
#set ( changable, will not have duplictes)
#dictionary(Key value pair) mutable

my_list = [1,2,2,3]
print(my_list)
my_set = {1,2,2,3,3,3,3}
print(my_set)
my_set.remove(3)
print(my_set)
my_set.add(89)
print(my_set)
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)
my_new_list = [4,4,4,5]
my_new_set = set(my_new_list)
print(my_new_set)

d = {1:"one",2:"two",3:"three",4:"four"}

print(d[1])
print(d[2])

"""
for key in d: # Iterates just through the keys, ignoring the values
for key, value in d.items(): # Iterates through the pairs
for key in d.keys(): # Iterates just through key, ignoring the values
for value in d.values(): # Iterates just through value, ignoring the keys
"""
print(d.keys())
for i in d.keys():
    print(f"{i} -- > {d[i]}")

for key, value in d.items():
    print(f"{key}  {value}")

for i in d.values()  :
    print(i)

d.update({4:'FOUR'})
for key, value in d.items():
    print(f"{key}  {value}")