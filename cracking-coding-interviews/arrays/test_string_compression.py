import unittest

# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3 . If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compression(string):

    if len(string) <= 0:
        return string

    current_char = string[0]
    counter = 0
    split_string = []

    for c in string:
        if current_char != c:
            split_string.append(current_char + str(counter))
            current_char = c
            counter = 0

        counter += 1

    split_string.append(current_char + str(counter))

    result = ('').join(split_string)

    if len(result) < len(string):
        return result

    return string

class SimpleTest(unittest.TestCase):
    def test_one_letters(self):
        test_string = "abcdefg"
        expected_result = "abcdefg"

        actual_result = compression(test_string)

        self.assertEqual(actual_result, expected_result)

    def test_oneletter(self):
        test_string = "aaaaaaaa"
        expected_result = "a8"

        actual_result = compression(test_string)

        self.assertEqual(actual_result, expected_result)

    def test_empty(self):
        test_string = ""
        expected_result = ""

        actual_result = compression(test_string)

        self.assertEqual(actual_result, expected_result)

    def test_basic(self):
        test_string = "aabcccccaaa"
        expected_result = "a2b1c5a3"

        actual_result = compression(test_string)

        self.assertEqual(actual_result, expected_result)
