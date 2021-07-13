import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition_method(self):
        test_data = CsvReader("src/Tests/Data/Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction_method(self):
        test_data = CsvReader("src/Tests/Data/Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication_method(self):
        test_data = CsvReader("src/Tests/Data/Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division_method(self):
        test_data = CsvReader("src/Tests/Data/Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.division(row['Value 2'], row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square_method(self):
        test_data = CsvReader("src/Tests/Data/Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root_method(self):
        test_data = CsvReader("src/Tests/Data/SquareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.squareRoot(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def tests_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
