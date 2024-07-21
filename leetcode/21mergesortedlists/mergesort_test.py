import unittest
from mergesort import listNodeToList, merge, listNodeHelper


class SimpleTest(unittest.TestCase):
    def test_ListNodeLeetCode1(self):

        linkedList1 = listNodeHelper([1, 2, 4])
        linkedList2 = listNodeHelper([1, 3, 4]) 

        expected = [1,1,2,3,4,4]
        actual = merge(linkedList1, linkedList2)

        self.assertEqual(expected, listNodeToList(actual))

    def test_ListNodeLeetCode2(self):

        linkedList1 = listNodeHelper([])
        linkedList2 = listNodeHelper([]) 

        expected = []
        actual = merge(linkedList1, linkedList2)

        self.assertEqual(expected, listNodeToList(actual))

    def test_ListNodeLeetCode3(self):

        linkedList1 = listNodeHelper([])
        linkedList2 = listNodeHelper([0]) 

        expected = [0]
        actual = merge(linkedList1, linkedList2)

        self.assertEqual(expected, listNodeToList(actual))
