from simple_calculator import SimpleCalculator
import unittest

class test_calculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(5, 5)
        self.assertEqual(result, 10)


    def test_subtraction(self):
        result = self.calc.subtract(5, 5)
        self.assertEqual(result, 0)

    
    def test_multiplication(self):
        result = self.calc.multiply(5, 5)
        self.assertEqual(result, 25)

    
    def test_division(self):
        result = self.calc.divide(5, 5)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()