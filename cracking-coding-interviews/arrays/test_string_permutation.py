import unittest

def is_permutation(main, check):

    if len(main) != len(check):
        return False

    return sorted(main) == sorted(check)

class SimpleTest(unittest.TestCase):
    def test_crude(self):
        main_string = "abzy"
        check_string = "zyba"

        expected_result = True

        actual_result = is_permutation(main_string, check_string)

        self.assertEqual(actual_result, expected_result)

    def test_same_len_no_perm(self):
        main_string = "abza"
        check_string = "zyba"

        expected_result = False 

        actual_result = is_permutation(main_string, check_string)

        self.assertEqual(actual_result, expected_result)

    def test_false(self):
        main_string = "abz"
        check_string = "zyba"

        expected_result = False

        actual_result = is_permutation(main_string, check_string)

        self.assertEqual(actual_result, expected_result)
