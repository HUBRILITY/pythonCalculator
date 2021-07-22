from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    num_values = len(data)
    total = num_values
    for num in data:
        total = addition(total, num)
    return division(num_values, total)
