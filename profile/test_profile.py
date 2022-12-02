import sys
import unittest
from io import StringIO
from profile import Profile


#for test functions that not reyurn values
class TestProfile(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile("yasi",25,"programmer")
        
        
    def test_name(self):
        self.profile.getName()
        self.assertEqual(sys.stdout.getvalue().strip(),"yasi")
    
    def test_age(self):
        self.profile.getAge()
        self.assertEqual(sys.stdout.getvalue().strip(),"25")
    
    def test_job(self):
        self.profile.getJob()
        self.assertEqual(sys.stdout.getvalue().strip(),"programmer")
    
    def tearDown(self):
        self.profile = None