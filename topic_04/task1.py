def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "На нуль ділити не можна!"

def calculator():
    print("Доступні операції: +, -, *, /")
    print("Введіть 'exit' для завершення програми.")

    while True:
        op = input("\nВиберіть операцію (+, -, *, /, exit): ")
        if op == "exit":
            print("Програма завершена.")
            break  

        try:
            a = int(input("Введіть перше число: "))
            b = int(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: введено не число!")
            continue

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
