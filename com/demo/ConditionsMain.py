m1 = 100
emp_name = "surender raja"

def main():
    print("main started")
    if(m1 <=100):
        print(f"{m1} is lesser or equal to  100")
        print("pass")
    else:
        print(f"{m1} is greater than  100")
    print("main ended")


def invoke_nested_if():
    if((m1>=0) & (m1<=100)):
        print(f"case 1 {m1} is less than 100")
    elif((m1>=100) & (m1<200)):
        print(f"case 2 {m1} is  greater than 100  and less than 200")
    elif((m1>=200) & (m1<300)):
        print(f"case 3 {m1} is   in  the  range of 200-300")
    else:
        print(f"case 4 {m1} is  greater than 300")


def string_condition():
    if(emp_name == 'surender'):
        print("yes, true")
    if(len(emp_name)== 8):
        print("yes, length is 8 ")
    else:
        print("no, length is not 8 ")


if __name__ == "__main__":
    print(f"The __name variable inside ConditionsMain is {__name__}")
    main()
    invoke_nested_if()
    string_condition()
    if(10 > 20):
        print("10>20")
    else:
        print("FALSEEEEEEE")


