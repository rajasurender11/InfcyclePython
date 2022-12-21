

n1 =30
m1= 590
id =888

def local_method():
    global m1
    id=76
    print(f"Inside local_method method , value of id is {id}")
    m1=m1+10
    print(f"Inside local_method method , value of m1 is {m1}")



def main():
    print("main method started")
    id =90
    a1 =98
    print(f"Inside main method , value of id is {id}")
    print(f"Inside main method , value of n1 is {n1}")
    print(f"Inside main method , value of m1 is {m1}")
    print("main method ended")


if __name__ == "__main__":
    print(f"The __name variable inside ConditionsMain is {__name__}")
    main()
    print(id)
    print(n1)
    local_method()
    print(m1)
    print(id)