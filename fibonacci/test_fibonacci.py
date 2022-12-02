import time
import unittest
from fibonacci import FibonacciSequense

class TestEfficiencyFibonacci(unittest.TestCase):
    
    def setUp(self):
        self._fibonacci_sequense = FibonacciSequense()
        self._efficiency_data = dict()
    
    def test_recursive_method(self):
        starting_time = time.time()
        
        self._fibonacci_sequense.recursive_method(35)
        
        ending_time = time.time()
        
        self._efficiency_data['recursive_method'] = ending_time - starting_time
            
    def test_math_method(self):
        starting_time = time.time()
        
        self._fibonacci_sequense.math_method(35)
        
        ending_time = time.time()
        
        self._efficiency_data['math_method'] = ending_time - starting_time
    
    def tearDown(self):
        print(self._efficiency_data)
        self._fibonacci_sequense = None
        self._efficiency_data.clear()