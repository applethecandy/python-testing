import unittest
from quadraticequation import *

class TestQuadraticEquation(unittest.TestCase):

    def testingtworoots(self):
        self.assertEqual(solveQuadraticEquation(5, -3, -2), [1, -0.4])
    
    def testingoneroot(self):
        self.assertEqual(solveQuadraticEquation(4, -12, 9), [1.5, 1.5])

    def testingnoroots(self):
        self.assertEqual(solveQuadraticEquation(5, 6, 7), [])

if __name__ == "__main__":
    unittest.main()