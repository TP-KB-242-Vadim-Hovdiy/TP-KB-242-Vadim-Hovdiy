from operations import Plus, Minus, Multiply, Divide 
class Calculator: 
    def __init__(self): 
        self.operations = { 
            '+': Plus(), 
            '-': Minus(), 
            '*': Multiply(), 
            '/': Divide() 
        } 

    def calculate(self, a, b, op):
        if op not in self.operations:
            raise ValueError("Невідома операція!")
        return self.operations[op].execute(a, b) 