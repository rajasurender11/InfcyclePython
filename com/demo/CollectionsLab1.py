
num_list = [2,8,9,4,90]
#mutable(changable) the values can be changed or
# added with new value , a value can be removed
str_list = ["surender","raja","Hadoop","python","spark"]
str_adv_list = ["100|surender|TCS","101|raja|CTS"]
mixed_list = ["surender",90,8.9,True,"raja"]

print(num_list)
print(num_list[0])
print(num_list[1])
print(num_list[len(num_list)-1])

#iterate
print(str_list[3])

for i in num_list:
    print(i)
    if(i%2 == 0):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


for i in str_list:
    print(i)
    if(len(i)%2 == 0):
        print(f"{i} with length {len(i)} is even")
    else:
        print(f"{i} with length {len(i)} is odd")


num_list.append(90)
print(num_list)
num_list.insert(2,67) # in 2nd index, the value 67 will be added
print(num_list)
num_list.remove(2)# value 2 will be removed
print(num_list)
num_list.pop(3) #3rd positioned value will be removed
print(num_list)
num_list.pop(len(num_list)-1)

num1_list = [8,9,5,2]

num1_tuple = (2,7,8) #immutable (you cannot change the value)

cn = len(num1_tuple)
print(cn)
print(num1_tuple[0])
print(num1_tuple[1])
print("***************TUPLE******************")
for i in num1_tuple:
    print(i)

converted_list =   list(num1_tuple)
converted_list.append(100)
a = tuple(converted_list)
for i in a:
    print(i)