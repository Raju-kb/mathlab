def myfunc(x):
    return 1/(1+x**2)

def trapezoidal(x0,xn,n):
    h = (xn - x0 )/n

    integrate = myfunc(x0) + myfunc(xn)
    for i in range(1,n):
        k =x0 + i * h
        integrate = integrate +2 * myfunc(k)
    integrate = integrate * h/2
    return integrate

lowerlimit = float(input("enter lower limitof integration : "))
upperlimit = float(input("enter upper limit of integration : "))
subinterval = int(input("enter numbe of sub intervals  : "))
result = trapezoidal(lowerlimit ,upperlimit,subinterval)
print("integration result by trapezoidal method is : ",result)
