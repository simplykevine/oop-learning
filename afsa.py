import math
def arguments(x,y):
    a=x*y
    b=pow(x,y)
    f=math.sqrt(x*y)
    print("the multiple of x*y = ", a)
    print("the power of x,y = ", b)
    print("the square root of x, y =", f)

c=int(input("enter the first number: "))
d=int(input("enter the second number: "))
arguments(c,d)



