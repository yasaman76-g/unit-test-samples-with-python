import unittest
from calculator_v2 import Calculator

class TestsCalculatorV2(unittest.TestCase):
    
    def setUp(self):
        print("setUp invoked")
        
    def tearDown(self):
        print("tearDown invoked")
        
    def test_add_functionality_v2(self):
        print(">>> test_add_functionality_v2")
        calculator = Calculator(20, 10)
        
        result = calculator.calc_add()
        
        self.assertEqual(result, 30)
        
    def test_add_functionality_tow_negative_numbers_v2(self):
        print(">>> test_add_functionality_tow_negative_numbers_v2")
        calculator = Calculator(-20, -10)
        
        result = calculator.calc_add()
        
        self.assertEqual(result, -30)
        
    def test_add_functionality_one_numbers_and_one_string_v2(self):
        print(">>> test_add_functionality_one_numbers_and_one_string_v2")
        calculator = Calculator(20,"Python")
        with self.assertRaises(TypeError):
            result = calculator.calc_add()
        
            self.assertEqual(result, 30)