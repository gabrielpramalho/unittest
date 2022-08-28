import unittest
import maxmin


class TestMaxMin(unittest.TestCase):
    def test_maxmin(self):
        self.assertEqual(maxmin.MaxMin([1, 2, 3]), [3,1])

    def test_maximun(self):
        self.assertEqual(maxmin.Max([1, 2, 3]), 3)

    def test_minimun(self):
        self.assertEqual(maxmin.Min([1, 2, 3]), 1)

    def test_maxmin_with_one_number(self):
        self.assertEqual(maxmin.MaxMin([3]), [3,3])
        

if __name__ == '__name__':
    unittest.main()