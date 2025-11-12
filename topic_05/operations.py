from functions import plus, minus, multiply, divide

def main():
    print("Доступні операції: +, -, *, /")
    print("Введіть 'exit' для завершення програми.")


    while True:
        op = input("\nВиберіть операцію (+, -, *, /, exit): ") 
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        if op == "exit":
            print("Програма завершена.")
            break  
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