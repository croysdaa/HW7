import FizzBuzz
import pytest
import unittest

class FizzBuzzTest(unittest.TestCase):
    
    def test_one(self):
       self.assertEqual(1, FizzBuzz.fizzbuzz_check(1))

    def test_threes(self):
        self.assertEqual("Fizz", FizzBuzz.fizzbuzz_check(9))

    def test_fives(self):
        self.assertEqual("Buzz", FizzBuzz.fizzbuzz_check(25))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", FizzBuzz.fizzbuzz_check(15))

if __name__ == '__main__':
    unittest.main()

