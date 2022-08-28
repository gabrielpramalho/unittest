import unittest
import main

class TestEquation(unittest.TestCase):
    def test_equation_two_roots(self):
        self.assertEqual(main.getRoots(1, 12, -13), [1.0, -13])

    def test_equation_one_root(self):
        self.assertEqual(main.getRoots(1, 2, 1), [-1.0])
        
    def test_equation_without_roots(self):
        self.assertEqual(main.getRoots(7, 3, 4), [])




if __name__ == '__name__':
    unittest.main()