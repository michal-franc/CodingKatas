import unittest
from invert import invertTree, createTreeFromArray

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testArrayRaw = [4, 2, 7, 1, 3, 6, 9]
        testArray = createTreeFromArray(testArrayRaw)

        expectedArrayRaw = [4, 7, 2, 9, 6, 3, 1]
        expectedArray = createTreeFromArray(expectedArrayRaw)

        actualArray = invertTree(testArray)

        self.assertEqual(expectedArray, actualArray)

    def test_example2(self):
        testArrayRaw = [2, 1, 3]
        testArray = createTreeFromArray(testArrayRaw)

        expectedArrayRaw = [2, 3, 1]
        expectedArray = createTreeFromArray(expectedArrayRaw)

        actualArray = invertTree(testArray)

        self.assertEqual(expectedArray, actualArray)
