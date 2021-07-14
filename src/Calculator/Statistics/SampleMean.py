from Calculator.Addition import addition
from Calculator.Division import division


def sample_mean(data, sample_size):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(total, num_values)
