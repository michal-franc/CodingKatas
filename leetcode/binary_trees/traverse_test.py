import unittest
from binarytree import createTreeFromArray
from traverse import preOrder, inOrder, postOrder, preOrderIterative, levelOrder

class BasicTestss(unittest.TestCase):
    def test_examplePreOrder1(self):
        testArrayRaw = [1, None, 2, 3]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [1, 2, 3]

        actual = preOrderIterative(testTree)

        self.assertEqual(expected, actual)

    def test_examplePreOrder2(self):
        testArrayRaw = []
        testTree = createTreeFromArray(testArrayRaw)

        expected = []

        actual = preOrder(testTree)

        self.assertEqual(expected, actual)

    def test_examplePreOrder3(self):
        testArrayRaw = [1]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [1]

        actual = inOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleInOrder1(self):
        testArrayRaw = [1, None, 2, 3]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [1, 3, 2]

        actual = inOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleInOrder2(self):
        testArrayRaw = []
        testTree = createTreeFromArray(testArrayRaw)

        expected = []

        actual = preOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleInOrder3(self):
        testArrayRaw = [1]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [1]

        actual = inOrder(testTree)

        self.assertEqual(expected, actual)

    def test_examplePostOrder1(self):
        testArrayRaw = [1, None, 2, 3]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [3, 2, 1]

        actual = postOrder(testTree)

        self.assertEqual(expected, actual)

    def test_examplePostOrder2(self):
        testArrayRaw = []
        testTree = createTreeFromArray(testArrayRaw)

        expected = []

        actual = postOrder(testTree)

        self.assertEqual(expected, actual)

    def test_examplePostOrder3(self):
        testArrayRaw = [1]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [1]

        actual = postOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleLevelOrder1(self):
        testArrayRaw = [3, 9, 20, None, None, 15, 7]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [[3], [9,20], [15,7]]

        actual = levelOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleLevelOrder2(self):
        testArrayRaw = []
        testTree = createTreeFromArray(testArrayRaw)

        expected = []

        actual = levelOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleLevelOrder3(self):
        testArrayRaw = [1]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [[1]]

        actual = levelOrder(testTree)

        self.assertEqual(expected, actual)

    def test_exampleLevelOrder4(self):
        testArrayRaw = [1,2,3,4,5]
        testTree = createTreeFromArray(testArrayRaw)

        expected = [[1], [2,3], [4,5]]

        actual = levelOrder(testTree)

        self.assertEqual(expected, actual)
