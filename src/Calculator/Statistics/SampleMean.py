from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Statistics.GetSample import getSample


def sample_mean(data, sample_size):
    total = 0

    # check that get sample returns proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than population

    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)
