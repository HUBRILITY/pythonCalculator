from Calculator.Calculator import Calculator
from Calculator.Statistics.Mean import mean
from Calculator.Statistics.SampleMean import sample_mean
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def sampleMean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result
