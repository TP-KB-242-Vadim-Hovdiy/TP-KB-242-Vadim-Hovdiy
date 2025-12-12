import math

# -------------------------------
def tokenize(expr):
    tokens = []
    i = 0
    length = len(expr)

    while i < length:
        ch = expr[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit() or ch == '.':
            num = ''
            dot_count = 0
            while i < length and (expr[i].isdigit() or expr[i] == '.'):
                if expr[i] == '.':
                    dot_count += 1
                    if dot_count > 1:
                        raise ValueError("Некоректне число: 2 крапки")
                num += expr[i]
                i += 1
            tokens.append(num)
            continue

        if ch in '+-':
            if (len(tokens) == 0 or tokens[-1] in "+-*/^("):
                sign = ch
                i += 1
                if i < length and (expr[i].isdigit() or expr[i] == '.'):
                    num = sign
                    dot_count = 0
                    while i < length and (expr[i].isdigit() or expr[i] == '.'):
                        if expr[i] == '.':
                            dot_count += 1
                            if dot_count > 1:
                                raise ValueError("Некоректне число з крапками")
                        num += expr[i]
                        i += 1
                    tokens.append(num)
                    continue
            tokens.append(ch)
            i += 1
            continue

        if ch in "*/^()":
            tokens.append(ch)
            i += 1
            continue

        raise ValueError(f"Невідомий символ '{ch}'")

    return tokens


# -------------------------------
def to_rpn(tokens):
    precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
    right_assoc = {'^'}

    output = []
    stack = []

    for tok in tokens:
        if tok.replace('.', '', 1).lstrip('+-').isdigit():
            output.append(tok)

        elif tok in precedence:
            while (stack and stack[-1] in precedence and
                   (precedence[stack[-1]] > precedence[tok] or
                   (precedence[stack[-1]] == precedence[tok] and tok not in right_assoc))):
                output.append(stack.pop())
            stack.append(tok)

        elif tok == '(':
            stack.append(tok)

        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Немає відкриваючої дужки")
            stack.pop()
        else:
            raise ValueError(f"Невідомий токен '{tok}'")

    while stack:
        if stack[-1] in "()":
            raise ValueError("Дужки не збалансовані")
        output.append(stack.pop())

    return output


# -------------------------------
def eval_rpn(rpn):
    stack = []

    for tok in rpn:
        if tok.replace('.', '', 1).lstrip('+-').isdigit():
            stack.append(float(tok))
            continue

        if tok in "+-*/^":
            if len(stack) < 2:
                raise ValueError("Недостатньо операндів")
            b = stack.pop()
            a = stack.pop()
            if tok == '+': stack.append(a + b)
            elif tok == '-': stack.append(a - b)
            elif tok == '*': stack.append(a * b)
            elif tok == '/':
                if b == 0:
                    raise ZeroDivisionError("Ділення на нуль")
                stack.append(a / b)
            elif tok == '^': stack.append(a ** b)
            continue

        raise ValueError(f"Невідомий оператор '{tok}'")

    if len(stack) != 1:
        raise ValueError("Помилка RPN послідовності")

    return stack[0]


# -------------------------------
def main():
    expr = input("Введіть вираз: ")

    try:
        tokens = tokenize(expr)
        rpn = to_rpn(tokens)
        print("RPN:", " ".join(rpn))

        result = eval_rpn(rpn)

        if abs(result - int(result)) < 1e-12:
            print("Результат:", int(result))
        else:
            print("Результат:", result)

    except Exception as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
