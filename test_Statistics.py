import unittest

from Calculator.Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics,)

    def test_mean_method(self):
        test_data = CsvReader("src/Tests/Data/sampleStatisticsData.csv").data
        result = self.statistics.mean(test_data, 0)
        self.assertEqual(result, 55.63)


if __name__ == '__main__':
    unittest.main()
