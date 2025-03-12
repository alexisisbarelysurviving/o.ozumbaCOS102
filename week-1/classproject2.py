P = float (input("enter principal amount: "))
R = float(input("enter rate: "))
n = float(input("enter number of times compounded: "))
t = float(input("enter time: "))

A = P*(1+R/n)**n*t
print (A)