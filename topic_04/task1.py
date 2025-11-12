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
 
def getCorrectOp():
    opList = ["+", "-", "*", "/", "q"]
    while True:
        op = input("Please enter the operation or q for exit: ")
        if op in opList:
            return op
        else:
            print("EROR: Wrong operation")
 
 
def getCorrecvtIntValue(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка: введено не число!")
 
def calculator():
    print("Доступні операції: +, -, *, /")
    print("Введіть 'exit' для завершення програми.")
 
    while True:
        op = getCorrectOp()
        if op == "q":
            print("Програма завершена.")
            break  
 
        a = getCorrecvtIntValue("Ведіть перше число -> ")
        b = getCorrecvtIntValue("Ведіть друге число -> ")
 
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

