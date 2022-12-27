
id =10


loc ="C:\\surender\\hadoop_course\\4_inputfiles\\accounts_profile.txt"
print(loc)
file = open(loc,"r")
data_list = file.readlines()
print(len(data_list))
for i in data_list:
    print(f"{i} --> {len(i)}  --> {i.split(',')}")
file.close()


f = open("C:\\surender\\hadoop_course\\4_inputfiles\\infycycle.txt", "a+")
f.write("\nWhat is your name ")
f.write("\nHow are you  ")
f.close()


