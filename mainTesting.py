import unittest
from main import StringCalculator


class StringCalculatorTestCase(unittest.TestCase):
    stringCalc = StringCalculator()

    def test_empty_string(self):
        result = self.stringCalc.add("")
        self.assertEqual(result, 0)
        result1 = self.stringCalc.add("2")
        self.assertEqual(result1, 2)
        result2 = self.stringCalc.add("22")
        self.assertEqual(result2, 22)
        result3 = self.stringCalc.add("2,5")
        self.assertEqual(result3, 7)
        result4 = self.stringCalc.add("21,6")
        self.assertEqual(result4, 27)
        result5 = self.stringCalc.add("2,5,6,7,8")
        self.assertEqual(result5, 28)
        result6 = self.stringCalc.add("21, 06, 7, 100, 050")
        self.assertEqual(result6, 184)
        result7 = self.stringCalc.add("1,2,a,c")
        self.assertEqual(result7, 7)
        result8 = self.stringCalc.add("22,x,6,b")
        self.assertEqual(result8, 54)
        result9 = self.stringCalc.add("1,999, 1000, 5, 1010")
        self.assertEqual(result9, 2005)
        result10 = self.stringCalc.add("1,999, 1000, 1001, 5")
        self.assertEqual(result10, 2005)

        result11 = self.stringCalc.add("1, 999\n1000, 5, 1010")
        self.assertEqual(result11, 2005)
        result12 = self.stringCalc.add("1,999, 1000\n1001, 5")
        self.assertEqual(result12, 2005)



    def test_empty_string(self):
        result13 = self.stringCalc.add("//;\n1;2")
        self.assertEqual(result13, 3)
        result14 = self.stringCalc.add("//++\n1++2++3++4\n5\n6++7++1001++a++c++")
        self.assertEqual(result14, 32)

        result15 = self.stringCalc.add("1//++\n1++2++3++4\n5\n6++7++1001++a++c")
        self.assertEqual(result15, 15)
        result16 = self.stringCalc.add("0//++\n1++2++3++4\n5\n6++7++1001++a++c")
        self.assertEqual(result16, 17)