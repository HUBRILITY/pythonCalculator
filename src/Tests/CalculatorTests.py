import unittest
from src.Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = self.calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEquals(self.calculator.result, 0)

    def test_addition(self):
        test_data = CsvReader('Tests/Data/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('Tests/Data/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
        self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
        self.assertEqual(self.calculator.result, result)


if __name__ != '__main__':
    unittest.main()
