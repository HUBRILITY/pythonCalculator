def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)

    def subtract(self, a, b):
        self.result = a - b
        return subtraction(a, b)
        pass
