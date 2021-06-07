import FizzBuzz
import pytest
import unittest

class FizzBuzzTest(unittest.TestCase):
    
    def test_one(self):
       self.assertEqual(1, FizzBuzz.fizzbuzz_check(1))

    def test_threes(self):
        self.assertEqual("Fizz", FizzBuzz.fizzbuzz_check(9))

if __name__ == '__main__':
    unittest.main()

