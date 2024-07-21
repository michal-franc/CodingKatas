import unittest
from maxsubarray import maxSubArray


class SimpleTest(unittest.TestCase):
    def test_leetcode1(self):

        testNums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6

        actual = maxSubArray(testNums)

        self.assertEqual(expected, actual)

    def test_leetcode2(self):

        testNums = [1]
        expected = 1

        actual = maxSubArray(testNums)

        self.assertEqual(expected, actual)

    def test_leetcode3(self):

        testNums = [5,4,-1,7,8]
        expected = 23

        actual = maxSubArray(testNums)

        self.assertEqual(expected, actual)
