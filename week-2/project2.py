import math
operation = input("enter the type of equation you would like to find the roots of: ")
if operation == 'quadratic':
    A = int(input("enter value of A: "))
    B = int(input("enter value of B: "))
    C = int(input("enter value of C: "))
    QE = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
    QE2 = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)

    print (QE)
    print (QE2)
elif operation == 'cubic':
    A = int(input("enter value of A: "))
    B = int(input("enter value of B: "))
    C = int(input("enter value of C: "))
    D = int(input("enter value of D: "))

    p = (3*A*C - B**2) / (3*A**2)
    q = (2*B**3 - 9*A*B*C + 27*A**2*D) / (27*A**3)

    inner_sqrt = math.sqrt((q / 2) ** 2 + (p / 3) ** 3)

    # Calculate the two cube roots
    u = (-q / 2) + inner_sqrt
    v = (-q / 2) - inner_sqrt

    # Cube roots, handling negative numbers correctly
    u_cbrt = math.copysign(abs(u) ** (1/3), u)
    v_cbrt = math.copysign(abs(v) ** (1/3), v)

    # Final root calculation
    QE3 = u_cbrt + v_cbrt - (B / (3 * A))

    print(QE3)
