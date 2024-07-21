import unittest
from substring import lengthOfLongestSubstring 

class BasicTestss(unittest.TestCase):
    def test_itReturns0Forempty(self):

        actual = lengthOfLongestSubstring("")

        self.assertEqual(actual, 0)

    def test_itReturns1Fors(self):

        actual = lengthOfLongestSubstring("s")

        self.assertEqual(actual, 1)

    def test_itReturns1Forss(self):

        actual = lengthOfLongestSubstring("ss")

        self.assertEqual(actual, 1)

    def test_itReturns2Forsa(self):

        actual = lengthOfLongestSubstring("sa")

        self.assertEqual(actual, 2)

    def test_itReturns2Forsa(self):

        actual = lengthOfLongestSubstring("ssa")

        self.assertEqual(actual, 2)

    def test_itReturns1Forbbbbbb(self):

        actual = lengthOfLongestSubstring("bbbbbb")

        self.assertEqual(actual, 1)

    def test_itReturns4Forpkwe(self):

        actual = lengthOfLongestSubstring("pkwe")

        self.assertEqual(actual, 4)

    def test_itReturns3Fordvdf(self):

        actual = lengthOfLongestSubstring("dvdf")

        self.assertEqual(actual, 3)

    def test_itReturns3Fordvddf(self):

        actual = lengthOfLongestSubstring("dvddf")

        self.assertEqual(actual, 2)
        
    def test_itReturns4Forabcdvdf(self):

        actual = lengthOfLongestSubstring("dabcdvdf")

        self.assertEqual(actual, 5)

    def test_itReturns3Forabcabcbb(self):

        actual = lengthOfLongestSubstring("abcabcbb")

        self.assertEqual(actual, 3)
