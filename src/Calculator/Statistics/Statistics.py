from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.datab)
        return self.result

    def sampleMean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a) -> object:
        self.result = square(a)
        return self.result

    def squareRoot(self, a):
        self.result = squareRoot(a)
        return self.result
