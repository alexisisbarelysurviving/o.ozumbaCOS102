PMT = float (input("enter amount of money paid (or received) in each period of the annuity: "))
R = float(input("enter rate: "))
n = float(input("enter number of times compounded: "))
t = float(input("enter time: "))

A = PMT*((1+R/n)**n*t -1)/(R/n)
print (A)