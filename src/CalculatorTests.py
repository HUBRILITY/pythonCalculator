import unittest
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = self.calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEquals(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/Addition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), float(row['Result'])

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)


if __name__ != '__main__':
    unittest.main()
