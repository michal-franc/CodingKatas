import unittest

def permutation_dict_counting(string):

    char_count = {}

    for c in string.lower():
        if c == ' ':
            continue

        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    found_one_odd = False

    for key in char_count:
        if char_count[key] % 2 != 0:
            if found_one_odd:
                return False
            found_one_odd = True

    return True

def permutation(string):

    checker = 0

    for c in string.lower():
        if c == ' ':
            continue

        # toggle bits if there are two letters that are the same bit will be zero
        checker = toggle_bit(checker, ord(c) - ord('a'))


    # if only one bit set then 
    # 00010000 - 1 = 00001111
    # 00010000 & 00001111 = 0
    return checker & (checker - 1) == 0

class SimpleTest(unittest.TestCase):
    def test_true(self):
        test = "    abcdabcd"

        expected_result = True

        actual_result = permutation(test)

        self.assertEqual(actual_result, expected_result)

    def test_false(self):
        test = "Tacx Coa"

        expected_result = False

        actual_result = permutation(test)

        self.assertEqual(actual_result, expected_result)

    def test_book(self):
        test = "Tact Coa"

        expected_result = True

        actual_result = permutation(test)

        self.assertEqual(actual_result, expected_result)

def toggle_bit(integer, offset):
    return integer ^ ( 1 << offset )

