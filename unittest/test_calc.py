import unittest
import Unit_Testing

# Test class
class TestCalc(unittest.TestCase):
    # Naming convention is required
    def test_add(self):
        self.assertEqual(Unit_Testing.add(10, 5), 15)
        self.assertEqual(Unit_Testing.add(-1, 1), 0)
        self.assertEqual(Unit_Testing.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(Unit_Testing.substract(10, 5), 5)
        self.assertEqual(Unit_Testing.substract(-1, 1), -2)
        self.assertEqual(Unit_Testing.substract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Unit_Testing.multiply(10, 5), 50)
        self.assertEqual(Unit_Testing.multiply(-1, 1), -1)
        self.assertEqual(Unit_Testing.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Unit_Testing.divide(10, 5), 2)
        self.assertEqual(Unit_Testing.divide(-1, 1), -1)
        self.assertEqual(Unit_Testing.divide(-1, -1), 1)
        self.assertEqual(Unit_Testing.divide(5, 2), 2.5)
        #self.assertRaises(ValueError, Unit_Testing.divide, 10, 0)

        # Context Manager
        with self.assertRaises(ValueError):
            Unit_Testing.divide(10, 0)

        

if __name__=='__main__':
    unittest.main()
