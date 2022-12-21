emp_str='surender|BNG|72500'

def main():
    emp_arr = emp_str.split("|")
    print(emp_arr)
    emp_name = emp_arr[0]
    emp_city = emp_arr[1]
    emp_sal = int(emp_arr[2])
    if(emp_city == 'CHN' and emp_sal >=50000):
        print("true")
    elif(emp_city == 'BNG' and emp_sal >= 50000 and emp_sal<= 75000):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    print(f"The __name variable inside ConditionsMain is {__name__}")
    main()