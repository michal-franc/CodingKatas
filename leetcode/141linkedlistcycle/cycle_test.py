import unittest
from node import *
from cycle import hasCycle 

class BasicTestss(unittest.TestCase):
    def test_example1(self):

        testList = [3, 2, 0, -4]
        head = createCyclicLinkedListFromArray(testList, 1)

        actual = hasCycle(head)
        expected = True 

        self.assertEqual(expected, actual)

    def test_example2(self):

        testList = [1, 2]
        head = createCyclicLinkedListFromArray(testList, 0)

        actual = hasCycle(head)
        expected = True 

        self.assertEqual(expected, actual)

    def test_example3(self):

        testList = [1, 2, 3, 4, 5, 6]
        head = createCyclicLinkedListFromArray(testList)

        actual = hasCycle(head)
        expected = False 

        self.assertEqual(expected, actual)
        
    def test_example4(self):

        testList = [1]
        head = createCyclicLinkedListFromArray(testList)

        actual = hasCycle(head)
        expected = False 

        self.assertEqual(expected, actual)

    def test_example5(self):

        testList = []
        head = createCyclicLinkedListFromArray(testList)

        actual = hasCycle(head)
        expected = False 

        self.assertEqual(expected, actual)

    def test_example6(self):

        testList = [1, 2, 1, 3]
        head = createCyclicLinkedListFromArray(testList, 0)

        actual = hasCycle(head)
        expected = True

        self.assertEqual(expected, actual)

    def test_example7(self):

        testList = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
        head = createCyclicLinkedListFromArray(testList, -1)

        actual = hasCycle(head)
        expected = False

        self.assertEqual(expected, actual)
