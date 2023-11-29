import unittest
import codefortesting

class TestCalculationsMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(7, codefortesting.add(2,5))

    def test_multiply(self):
        self.assertEqual(10, codefortesting.multiply(2,5))

    def test_power(self):
        self.assertEqual(256, codefortesting.power(2,8))

    def testShouldNotReturnSeven(self):
        self.assertNotEqual(7, codefortesting.add(2,9))
    
    
if __name__ == '__main__':
    unittest.main()