id =20
emp_name = "surender"
m1=20
m2=40
m3=50


def process():
    print(id)
    print(m1)

def data_process(a,b):
    c =a+b
    print(c)
    return c


def data_dummy_process(a,b):
    print(f"This is data_dummy_process method {a}")
    c =5+6
    print(c)

process()
print(id)
print(data_process(4,5))
result = data_process(8,9)
data_dummy_process(result,8)
data_process(m1,m2)