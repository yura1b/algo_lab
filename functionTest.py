import unittest

from main import find_kth_largest


class TestFindKElementAndPosition(unittest.TestCase):

    def test_find_k_element_and_its_position(self):
        arr3 = [4, 8, 2, 10, 6]
        k3 = 3
        expected_output3 = 8
        self.assertEqual(findKthLargest(arr3, k3), expected_output3)

        arr4 = []
        k4 = 2
        expected_output4 = None
        self.assertEqual(findKthLargest(arr4, k4), expected_output4)


if __name__ == '__main__':
    unittest.main()
