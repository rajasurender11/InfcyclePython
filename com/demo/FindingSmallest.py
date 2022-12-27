
my_list = [4,2,6,7,8,0,8]
sorted_list = sorted(my_list)
print(sorted_list)
print(sorted_list[0])

min_value = my_list[0] #4

for i in my_list:
    if (i >min_value): #4<4  2 <4 6 <2 7 <2
        min_value = i

print(min_value)

sum_result = 0
for i in range(0,10,2):

    sum_result = sum_result+i
print(sum_result)


num =  134
num_str = str(num)

if(int(num_str[1:2])%2 == 0 ):
    print("EVEN")
else:
    print("ODD")