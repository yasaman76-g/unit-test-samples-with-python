from math import sqrt

class FibonacciSequense:
    
    def recursive_method(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        return self.recursive_method(n - 1) + self.recursive_method(n - 2)
    
    def math_method(self,n):
        return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n / (2 ** n * sqrt(5)))