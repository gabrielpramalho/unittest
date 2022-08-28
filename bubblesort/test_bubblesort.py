import unittest
import bubblesort as bs


class TestBubbleSort(unittest.TestCase):
    
    def test_bubblesort(self):
        self.assertEqual(bs.bubblesort([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5])
    def test_bubblesort_one_number(self):
            self.assertEqual(bs.bubblesort([1]), [1])
    def test_bubblesort_without_numbers(self):
            self.assertEqual(bs.bubblesort([]), [])

if __name__ == '__name__':
    unittest.main()