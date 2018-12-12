import unittest
from factorial import Factorial

class FacTest(unittest.TestCase):
    def testNegative(self):
        self.assertEqual(Factorial(-1).fac(), "Please enter an int greater or equals 0")
    def testLetters(self):
        self.assertEqual(Factorial("a").fac(), "Please enter an int greater or equals 0")
    def testCharacters(self):
        self.assertEqual(Factorial("@").fac(), "Please enter an int greater or equals 0")
    def testPosNum(self):
        self.assertEqual(Factorial(1).fac(), 1)
if __name__ == '__main__':
    unittest.main()