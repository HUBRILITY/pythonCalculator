from Calculator.Calculator import Calculator
from Calculator.Statistics.Mean import mean
from Calculator.Statistics.SampleMean import sample_mean
from Calculator.Statistics.Median import median
from Calculator.Statistics.Mode import mode
from Calculator.Statistics.StandardDeviation import standard_dev
from Calculator.Statistics.Variance import variance
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        super().__init__()
        self.data = CsvReader(filepath)

    def mean(self):
        mean(self.data)

    def sampleMean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result

    def standard_dev(self):
        self.result = standard_dev(self.data)
        return self.result

    def variance(self):
        self.result = variance(self.data)
        return self.result
