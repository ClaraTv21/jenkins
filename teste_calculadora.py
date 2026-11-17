import unittest
from calculadora import soma, multiplica

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_multiplica(self):
        self.assertEqual(multiplica(4, 5), 20)

if __name__ == "__main__":
    unittest.main()