from calc import Calculator

def main():
    calc = Calculator()

    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            op = input("Операція (+, -, *, /): ")

            result = calc.calculate(a, b, op)
            print("Результат:", result)

        except Exception as e:
            print("Помилка:", e)


if __name__ == "__main__":
    main()
