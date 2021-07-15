from Calculator.Addition import addition
from Calculator.Division import division


def sample_mean(data, sample_size):
    num_values = len(data)
    total = 0
    random_values = random.choice(data, k=sample_size-1))
    for num in random_values:
        total = addition(total, num)
    return division(total, num_values)
