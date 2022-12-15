
emp_name = "surender raja"

len_str = len(emp_name)

print(f"The  string {emp_name} is of length {len_str}")

print(emp_name[2:7])
print(emp_name[0:7])
print(emp_name[0:])
print(emp_name[3:])
print(emp_name[0:-2])
print(emp_name[-12:-1])

current_date = "2022-12-15"
current_year = current_date[0:4]
print(current_year)

current_month = current_date[5:7]
print(current_month)

current_day = current_date[8:10]
print(current_day)

res_arr = current_date.split("-")

print(res_arr)

print(res_arr[0])
print(res_arr[1])
print(res_arr[2])

print(len(res_arr))


print(current_date.split("-")[0])



"""
print(s2[2:6])
print(s2[2:])
print(s2[:6])
"""

my_list = [10,20,40,6,8,0]
my_str = ["surender","raja",78.9,9]

replaced_str = emp_name.replace("raja","#")
print(replaced_str)

r3 =emp_name.startswith("S")
print(r3)

r4 = emp_name.upper()
print(r4)

print(emp_name[2:len(emp_name[0:12].split(" ")[0])])

print(emp_name.index("raja"))

print(emp_name[0:8].isalpha())
print(emp_name.isalnum())
print(emp_name.isnumeric())
print(emp_name.isspace())

for i in emp_name:
    print(i)