class  Plus:
    def execute(self, a, b):
        return a + b


class Minus:
    def execute(self, a, b):
        return a - b


class Multiply:
    def execute(self, a, b):
        return a * b


class Divide:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль!")
        return a / b
