import unittest
from numpy.random import seed
from

from Calculator.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_method(self):
        test_data = CsvReader("src/Tests/Data/Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)



    def tests_results_property(self):
        self.assertEqual(self.statistics.result, 0)


if __name__ == '__main__':
    unittest.main()
