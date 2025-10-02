def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

def calculator():
    print("Доступні операції: +, -, *, /")

    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    op = input("Виберіть операцію (+, -, *, /): ")

    match op:
        case "+":
            result = plus(a, b)
        case "-":
            result = minus(a, b)
        case "*":
            result = multiply(a, b)
        case "/":
            result = divide(a, b)
        case _:
            result = "Невідома операція!"

    print("Результат:", result)

calculator()