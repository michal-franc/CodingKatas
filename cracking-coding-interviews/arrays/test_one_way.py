import unittest

def one_way(first_string, second_string):

    if  abs(len(first_string) - len(second_string)) > 1:
        return False

    first_counter = 0
    second_counter = 0
    found_one_diff = False

    for _ in range(max(len(first_string), len(second_string))):

        if not found_one_diff:
            if first_counter + 1 >= len(first_string) or second_counter + 1 >= len(second_string):
                break

        if first_string[first_counter] != second_string[second_counter]:
            if found_one_diff:
                return False

            found_one_diff = True

            if first_string[first_counter + 1] == second_string[second_counter]:
                first_counter += 1
                continue

            if first_string[first_counter] == second_string[second_counter + 1]:
                second_counter += 1
                continue

        first_counter += 1
        second_counter += 1

        if first_counter >= len(first_string) or second_counter >= len(second_string):
            break


    return True

class SimpleTest(unittest.TestCase):
    def test_short(self):
        first = "p"
        second = ""

        expected_result = True

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_long(self):
        first = "pale"
        second = "paleeeeeeeeessfff"

        expected_result = False

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_pale_palf(self):
        first = "pale"
        second = "palf"

        expected_result = True

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_pale_bae(self):
        first = "pale"
        second = "bae"

        expected_result = False

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_pale_bale(self):
        first = "pale"
        second = "bale"

        expected_result = True

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_pale_ple(self):
        first = "pale"
        second = "ple"

        expected_result = True

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_pales_pale(self):
        first = "pales"
        second = "pale"

        expected_result = True

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_more_than_1_based_on_len(self):
        first = "paleta"
        second = "ple"

        expected_result = False

        actual_result = one_way(first, second)

        self.assertEqual(actual_result, expected_result)
