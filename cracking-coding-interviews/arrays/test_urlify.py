#https://waymoot.org/home/python_string/ URLify: Write a method to replace all spaces in a string with '%2e: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

# Efficient String Concatenation in Python - https://waymoot.org/home/python_string/
import unittest

def check_space(c):
    if c == ' ':
        return '%20'

    return c

def list_comprehension(inp):
    return ''.join([check_space(c) for c in inp])

def count_spaces(inp, length):
    counter = 0
    for i in range(length):
        if inp[i] == ' ':
            counter += 1

    return counter


def char_array(inp, length):

    index = length + (count_spaces(inp, length)) * 2
    res = [' '] * index
    for i in range(length - 1, -1, -1):
        if inp[i] == ' ':
            res[index - 3:index] = '%20'
            index -= 3
        else:
            res[index - 1] = inp[i]
            index -= 1

    return ''.join(res)

def urlify(inp, length):
    return char_array(inp, length)

class SimpleTest(unittest.TestCase):
    def test_book(self):
        inp = "Mr John Smith   "
        expected = "Mr%20John%20Smith"

        actual = urlify(inp, 13)

        self.assertEqual(actual, expected)

    def test_empty(self):
        inp = ""
        expected = ""

        actual = urlify(inp, 0)

        self.assertEqual(actual, expected)
        
    def test_one_space(self):
        inp = "abc def"
        expected = "abc%20def"

        actual = urlify(inp, 7)

        self.assertEqual(actual, expected)

    def test_two_spaces(self):
        inp = "abc  def"
        expected = "abc%20%20def"

        actual = urlify(inp, 8)

        self.assertEqual(actual, expected)

    def test_multi_spaces(self):
        inp = "        "
        expected = ""

        actual = urlify(inp, 0)

        self.assertEqual(actual, expected)

    def test_spaces_starta_and_end(self):
        inp = "   abc  def    "
        expected = "%20%20%20abc%20%20def"

        actual = urlify(inp, 11)

        self.assertEqual(actual, expected)
