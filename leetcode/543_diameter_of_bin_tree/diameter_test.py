import unittest
from diameter import createTreeFromArray, diameterOfBinaryTree

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testArrayRaw = [1, 2, 3, 5, 5]
        testTree = createTreeFromArray(testArrayRaw)

        expectedDiam = 3

        actualDiam = diameterOfBinaryTree(testTree)

        self.assertEqual(expectedDiam, actualDiam)

    def test_example2(self):
        testArrayRaw = [1, 2]
        testTree = createTreeFromArray(testArrayRaw)

        expectedDiam = 1

        actualDiam = diameterOfBinaryTree(testTree)

        self.assertEqual(expectedDiam, actualDiam)
