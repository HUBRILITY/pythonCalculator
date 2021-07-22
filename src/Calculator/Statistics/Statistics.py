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

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def sampleMean(self, sample_size):
        sample_mean(self.data, sample_size)

    def median(self):
        median(self.data)

    def mode(self):
        mode(self.data)

    def standard_dev(self):
        standard_dev(self.data)

    def variance(self):
        variance(self.data)
