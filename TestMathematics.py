import unittest
import random
from Mathematics import mathematics

class TestMathematics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mathIns = mathematics()

    def setUp(self):
       self.a = random.randint(1, 100)
       self.b = random.randint(1, 100)
       self.sum = self.a + self.b

    def test_add(self):
        result = self.mathIns.addition(self.a, self.b)
        print(self.sum)
        self.assertEqual(result, self.sum)

    def test_addition(self):
        result = self.mathIns.addition(self.a, self.b)
        print(self.sum)
        self.assertEqual(result, self.sum)
        
if __name__ == "__main__":
    unittest.main()