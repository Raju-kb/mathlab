def myfunc(x):
    return 1/(1+x**2)

def simpson(x0,xn,n):
    h= (xn - x0 )/n
    integrate = myfunc(x0) + myfunc(xn)
    k = x0
    for i in range(1,n):
        if i%2 == 0:
            integrate = integrate +4*myfunc(k)
        else:
            integrate = integrate +2*myfunc(k)
        k +=h
    integrate = integrate *h *(1/3)
    return integrate

lowerlimit = float(input("enter lower limit of integration :"))
upperlimit = float(input("enter upper limit of integration :"))
subinterval = int(input("enter number of sub intervals :"))
result = simpson(lowerlimit,upperlimit,subinterval)
print("integration result by simpson 1/3rd rule method :%0.6f " %(result))
