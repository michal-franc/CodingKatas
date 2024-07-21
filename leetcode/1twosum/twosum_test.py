import unittest
from twosum import twoSum

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        nums = [2,7,11,15] 
        target = 9 
        expected = [0,1]

        actual = twoSum(nums, target)

        self.assertEqual(expected, actual)

    def test_example2(self):
        nums = [3,2,4] 
        target = 6
        expected = [1,2]

        actual = twoSum(nums, target)

        self.assertEqual(expected, actual)

    def test_example3(self):
        nums = [3,3] 
        target = 6
        expected = [0,1]

        actual = twoSum(nums, target)

        self.assertEqual(expected, actual)
