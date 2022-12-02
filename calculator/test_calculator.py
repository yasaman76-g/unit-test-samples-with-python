import unittest
import calculator

class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(20, 10)
        
        self.assertEqual(result, 30)
        
    def test_add_functionality_tow_negative_numbers(self):
        result = calculator.calc_add(-20, -10)
        
        self.assertEqual(result, -30)