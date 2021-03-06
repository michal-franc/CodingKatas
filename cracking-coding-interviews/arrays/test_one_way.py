import unittest

# there are two cases
# either strings are of the same length -> then we just count the differences in chars
# one of the string is smaller by 1 -> and if diff we shift the index of the 'bigger' one
# this is O(n)

def one_way(first_string, second_string):

    # if len is bigger than 1 then there are more than 1 differences
    if  abs(len(first_string) - len(second_string)) > 1:
        return False

    if  min(len(first_string), len(second_string)) == 0:
        return True

    first_index = 0
    second_index = 0
    found_one_diff = False

    first_bigger = len(first_string) > len(second_string)
    are_equal = len(first_string) == len(second_string)

    for _ in range(max(len(first_string), len(second_string))):
        if first_string[first_index] != second_string[second_index]:
            if found_one_diff:
                return False

            found_one_diff = True

            if not are_equal:
                if first_bigger:
                    first_index += 1
                    continue
                else:
                    second_index += 1
                    continue

        first_index += 1
        second_index += 1

        if first_index >= len(first_string) or second_index >= len(second_string):
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

    def test_pale_paef(self):
        first = "pale"
        second = "paef"

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
