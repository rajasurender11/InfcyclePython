#write a python program to find ou the smallest number in this list
my_list = [78,5,2,89,0,78,5,-9]
min_value = my_list[0] #78 #5 #2
max_value= my_list[0]
for i in my_list:
    if(i<min_value):
        min_value = i

print(f"The smallest number is {min_value}")

for i in my_list:
    if(i>max_value):
        max_value = i

print(f"The highest number is {max_value}")