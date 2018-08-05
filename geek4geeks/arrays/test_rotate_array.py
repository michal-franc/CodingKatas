import unittest

def rotate(arr, pivot):

    split_right = arr[:pivot]
    split_left = arr[pivot:]

    return split_left + split_right

class SimpleTest(unittest.TestCase):
    def test_empty_array(self):
        rotate_by = 2
        test_arr = []
        expected_arr = []

        actual_arr = rotate(test_arr, rotate_by)

        self.assertEqual(expected_arr, actual_arr)

    def test_rotate_by_two(self):
        rotate_by = 2
        test_arr = [1, 2, 3, 4, 5]
        expected_arr = [3, 4, 5, 1, 2]

        actual_arr = rotate(test_arr, rotate_by)

        self.assertEqual(expected_arr, actual_arr)
