
#list in python
numbers_list = [2,4,12,0,99] #0th 1st 2nd 3rd
id = 10
s ="surender"
f =True
d = 12.89

length_of_list = len(numbers_list)
print(length_of_list)
print(numbers_list[0])
print(numbers_list[1])
print(numbers_list[2])
print(numbers_list[length_of_list-1])



print("*****************************")

#while loop for loop
n =0
#0<4  n=1  1<4 n=2 2<4  n=3 3<4 n=4 4<4
while(n<length_of_list):
  print(numbers_list[n])
  num = numbers_list[n]
  if(num%2 == 0):
      print("EVEN NUMBER")
  else:
      print("ODD NUMBER")
  n= n+1

print("FOR LOOP *********************************************")
for i in numbers_list:
    print(i)
    if(i > 10):
        print("BIGGER NUMBER")
    else:
        print("SMALLER NUMBER")


