import unittest

def permutation(string):

    char_count = {}
    length_no_spaces = 0

    for c in string.lower():
        if c == ' ':
            continue

        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

        length_no_spaces += 1

    if length_no_spaces % 2 == 0:
        for key in char_count:
            if char_count[key] % 2 != 0:
                return False
    else:
        one_odd = True
        for key in char_count:
            if char_count[key] % 2 != 0:
                if one_odd:
                    one_odd = False
                    continue
                return False

    return True

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

