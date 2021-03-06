import LeapYear 
import unittest

class LeapYearTest(unittest.TestCase):

    def test_divByFour(self):
       self.assertTrue(LeapYear.leapyear_check(4))

    def test_notDivByHundred(self):
        self.assertFalse(LeapYear.leapyear_check(100))
    
    def test_divByFourHundred(self):
        self.assertTrue(LeapYear.leapyear_check(400))

if __name__ == '__main__':
    unittest.main()

