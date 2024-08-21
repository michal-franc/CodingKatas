import unittest
from anagram import isAnagram

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testData1 = "anagram"
        testData2 = "nagaram"

        expected = True

        actual = isAnagram(testData1, testData2)

        self.assertEqual(expected, actual)

    def test_example2(self):
        testData1 = "car"
        testData2 = "rat"

        expected = False

        actual = isAnagram(testData1, testData2)

        self.assertEqual(expected, actual)

