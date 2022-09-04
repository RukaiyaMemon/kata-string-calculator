import unittest
from main import StringCalculator


class StringCalculatorTestCase(unittest.TestCase):
    stringCalc = StringCalculator()

    def test_empty_string(self):
        result = self.stringCalc.add("")
        self.assertEqual(result, 0)