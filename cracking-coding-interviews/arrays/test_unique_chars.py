import unittest

def using_dict(string):
    lookup = {}

    for single_char in string:
        if single_char in lookup:
            return False

        lookup[single_char] = True

    return True

def using_bits_int(string):
    bit_holder = 0

    for single_char in string:
        c_bit = ord(single_char) - ord('a')
        if ((bit_holder & (1 << c_bit)) > 0):
            return False
        bit_holder |= (1 << c_bit)

    return True

def is_unique(string):
    return using_bits_int(string)

class SimpleTest(unittest.TestCase):
    def test_crude(self):
        test_string = "abcdd"
        expected_result = False

        actual_result = is_unique(test_string)

        self.assertEqual(actual_result, expected_result)

    def test_empty(self):
        test_string = ""
        expected_result = True

        actual_result = is_unique(test_string)

        self.assertEqual(actual_result, expected_result)

    def test_correct(self):
        test_string = "abcd"
        expected_result = True

        actual_result = is_unique(test_string)

        self.assertEqual(actual_result, expected_result)

    def test_special_characters(self):
        test_string = "abcefghi"
        expected_result = True

        actual_result = is_unique(test_string)

        self.assertEqual(actual_result, expected_result)
