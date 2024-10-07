import unittest
from binarytree import createTreeFromArray
from construct import construct_in_post, construct_in_pre

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        actual = construct_in_post([9,3,15,20,7], [9,15,7,20,3])
        expectedArr = [3,9,20,None,None,15,7]
        expectedTree = createTreeFromArray(expectedArr)

        self.assertEqual(expectedTree, actual)

    def test_example2(self):
        actual = construct_in_pre([3,9,20,15,7], [9,3,15,20,7])
        expectedArr = [3,9,20,None,None,15,7]
        expectedTree = createTreeFromArray(expectedArr)

        print(actual)

        self.assertEqual(expectedTree, actual)
