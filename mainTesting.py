import unittest
from main import StringCalculator
class StringCalculatorTestCase(unittest.TestCase):
    stringCalc = StringCalculator()
    def test_empty_string(self):
        result = self.stringCalc.add("")
        result1 = self.stringCalc.add("2")
        result2 = self.stringCalc.add("22")
        result3 = self.stringCalc.add("2,5")
        result4 = self.stringCalc.add("21,6")
        self.assertEqual(result, 0)
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 22)
        self.assertEqual(result3, 7)
        self.assertEqual(result4, 27)