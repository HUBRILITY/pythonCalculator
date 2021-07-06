def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
