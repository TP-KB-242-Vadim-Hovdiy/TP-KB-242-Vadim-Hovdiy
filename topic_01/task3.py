def disc(a, b, c):
    return b*b - 4*a*c 
a = int(input("Значення A: "))
b = int(input("Значення B: "))
c = int(input("Значення C: "))
D = disc(a, b, c)
print("Дискримінант =", D)