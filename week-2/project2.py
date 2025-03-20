import cmath
operation = input("enter the type of equation you would like to find the roots of: ")
if operation == 'quadratic':
    A = int(input("enter value of A: "))
    B = int(input("enter value of B: "))
    C = int(input("enter value of C: "))
    QE = (-B + cmath.sqrt(B**2 - 4*A*C)) / (2*A)
    QE2 = (-B - cmath.sqrt(B**2 - 4*A*C)) / (2*A)

    print (QE)
    print (QE2)
elif operation == 'cubic':
    A = int(input("enter value of A: "))
    B = int(input("enter value of B: "))
    C = int(input("enter value of C: "))
    D = int(input("enter value of D: "))

    p = (3*A*C - B**2) / (3*A**2)
    q = (2*B**3-9*A*B*C+27*A**2*D) / (27*A**3)

    

    QE = (-B + cmath.sqrt(B**2 - 4*A*C)) / (2*A)
    QE2 = (-B - cmath.sqrt(B**2 - 4*A*C)) / (2*A)

    print (QE)
    print (QE2)
     