import unittest

# task:
# Given a string, that contains special character together with alphabets a to z and A to Z
# reverse the string in a way that special characters are not affected

# special character everything exept abc - example: space, dot, comman, $
# normal character - a to z and A to Z

# test scenarios from the easiest to the hardest:
# [] => []
# [a] => [a]
# [abc] => [cba]
# [ab,c] => [cb,a] -> 1 special
# [a,b$c] => [c,b$a]
# [,,,,] => [,,,,] -> only special

# easiest implementation
# one loop to get subsequence
# one loop to reverse
# one loop to add reversed items to the array
# but this is 3*O(n)

# better implementation
# one loop two indexes one starting at the beggingin the other at the end
# this should potentialy be O(n) only with 2 variables

def reverse(arr):
    length = len(arr)

    if length <= 0:
        return arr

    start = 0
    end = length - 1

    while start < end:
        # if one is special then dont advance this one and dont swap
        if arr[start].isalpha() and arr[end].isalpha():
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        if not arr[end].isalpha():
            end -= 1

        if not arr[start].isalpha():
            start += 1

    return arr

class SimpleTest(unittest.TestCase):

    def test_one_special_odd(self):
        test_arr = ['a', 'b', 'c', ',', 'd']
        expected_arr = ['d', 'c', 'b', ',', 'a']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_only_special(self):
        test_arr = [',', ',', ',', '%']
        expected_arr = [',', ',', ',', '%']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_one_special(self):
        test_arr = ['a', 'b', ',', 'c']
        expected_arr = ['c', 'b', ',', 'a']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_empty_array(self):
        test_arr = []
        expected_arr = []

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_single_array(self):
        test_arr = ['a']
        expected_arr = ['a']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_no_special_odd(self):
        test_arr = ['a', 'b', 'c', 'd']
        expected_arr = ['d', 'c', 'b', 'a']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_no_special(self):
        test_arr = ['a', 'b', 'c']
        expected_arr = ['c', 'b', 'a']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)

    def test_no_special_long(self):
        test_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        expected_arr = ['g', 'f', 'e', 'd', 'c', 'b', 'a']

        actual_arr = reverse(test_arr)
        self.assertEqual(expected_arr, actual_arr)
