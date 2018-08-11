import unittest

def permutation(string):

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

