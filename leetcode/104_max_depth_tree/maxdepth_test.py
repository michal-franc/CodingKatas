import unittest
from maxdepth import createTreeFromArray, maxDepth

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testArrayRaw = [3, 9, 20, None, None, 15, 7]
        testTree = createTreeFromArray(testArrayRaw)

        expectedDepth = 3

        actualDepth = maxDepth(testTree, 0)

        self.assertEqual(expectedDepth, actualDepth)
