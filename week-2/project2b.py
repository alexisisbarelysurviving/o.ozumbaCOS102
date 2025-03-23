import cmath  # Supports complex numbers

def solve_cubic(a, b, c, d):
    if a == 0:
        print("This is not a cubic equation.")
        return None

    # Convert to depressed cubic t^3 + pt + q = 0
    f = ((3 * c / a) - (b ** 2 / a ** 2)) / 3
    g = ((2 * b ** 3 / a ** 3) - (9 * b * c / a ** 2) + (27 * d / a)) / 27
    h = (g ** 2) / 4 + (f ** 3) / 27

    print(f"Depressed cubic coefficients: f = {f}, g = {g}, h = {h}")

    if h > 0:
        # One real root and two complex roots
        R = -(g / 2) + cmath.sqrt(h)
        S = R ** (1/3)
        T = -(g / 2) - cmath.sqrt(h)
        T = T ** (1/3)

        x1 = (S + T) - (b / (3 * a))
        x2 = -(S + T) / 2 - (b / (3 * a)) + (S - T) * cmath.sqrt(3) * 1j / 2
        x3 = -(S + T) / 2 - (b / (3 * a)) - (S - T) * cmath.sqrt(3) * 1j / 2

    elif h == 0:
        # All roots real, at least two are equal
        S = (g / 2) ** (1/3)

        x1 = -2 * S - (b / (3 * a))
        x2 = S - (b / (3 * a))
        x3 = x2

    else:
        # All roots real and unequal
        i = cmath.sqrt((g ** 2 / 4) - h)
        j = i ** (1/3)
        k = cmath.acos(-(g / (2 * i)))
        L = -j
        M = cmath.cos(k / 3)
        N = cmath.sqrt(3) * cmath.sin(k / 3)
        P = -(b / (3 * a))

        x1 = 2 * j * cmath.cos(k / 3) - (b / (3 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

    return x1, x2, x3

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))

roots = solve_cubic(a, b, c, d)

if roots:
    print("\nRoots of the cubic equation are:")
    for i, root in enumerate(roots, 1):
        print(f"x{i} = {root.real:.5f}" + (f" + {root.imag:.5f}i" if root.imag != 0 else ""))
