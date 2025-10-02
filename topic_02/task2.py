def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "На нуль ділити не можна"

print("Оберіть операцію:")
print("1 - Додавання (+)")
print("2 - Віднімання (-)")
print("3 - Множення (*)")
print("4 - Ділення (/)")

choice = input("Введіть номер операції (1/2/3/4): ")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

if choice == "1":
    print("Результат:", plus(a, b))
elif choice == "2":
    print("Результат:", minus(a, b))
elif choice == "3":
    print("Результат:", multiply(a, b))
elif choice == "4":
    print("Результат:", divide(a, b))
else:
    print("Невірний вибір!")
