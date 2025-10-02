def disc(a, b, c):
    return b*b - 4*a*c 
a = int(input("Значення A: "))
b = int(input("Значення B: "))
c = int(input("Значення C: "))
D = disc(a, b, c)
print("Дискримінант =", D) 
def roots(a, b, c):
    D = disc(a, b, c)
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return ()