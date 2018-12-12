import unittest
from factorial import Factorial

class FacTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Factorial(0).fac(), 1)

if __name__ == '__main__':
    unittest.main()