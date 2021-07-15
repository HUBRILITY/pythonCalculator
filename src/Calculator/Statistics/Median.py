

def median(data):
    n = len(data)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(data)[index]
    # Sample with an even number of observations
    return sum(sorted(data)[index - 1:index + 1]) / 2
