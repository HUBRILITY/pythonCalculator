class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result = x
        pass

    @staticmethod
    def add(a, b):
        c = a + b
        return c
