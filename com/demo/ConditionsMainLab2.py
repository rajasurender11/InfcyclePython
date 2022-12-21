a = 20
b = 37

def odd_or_even(num):
    if(num%2 == 0):
        return "EVEN"
    else:
        return "ODD"


def add_two_numbers():
    c= a+b
    return c

def main():
    r = add_two_numbers()
    result =odd_or_even(r)
    print(f"The result is {result}")


if __name__ == "__main__":
    print(f"The __name variable inside ConditionsMain is {__name__}")
    main()
