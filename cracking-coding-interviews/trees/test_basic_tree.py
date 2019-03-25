import unittest

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # first element case - it has to be pivot as we dont balance this tree
        if self.root is None:
            self.root = Node(value)
            return

        # leaf of the root case
        self.__insert_rec(self.root, value)

    def __insert_rec(self, level_root, value):
        # value less equal root move to left
        if value <= level_root.data:
            if level_root.left is None:
                level_root.left = Node(value)
            else:
                self.__insert_rec(level_root.left, value)

        if value > level_root.data:
            if level_root.right is None:
                level_root.right = Node(value)
            else:
                self.__insert_rec(level_root.right, value)


def arr_to_bst(arr):
    # we sort the array in reverse to simplify the problem
    # reverse as this will create balanced 'tree'
    sorted_arr = sorted(arr, reverse=True)

    bst = Bst()

    # move median as first element
    median_index = int(len(arr)/2)
    median_first = [sorted_arr[median_index]] + sorted_arr[0:median_index] + sorted_arr[median_index + 1:]

    print(median_first)

    for i in median_first:
        bst.insert(i)

    return bst

class FuncTest(unittest.TestCase):
    def test_bst_from_array(self):
        
        # sorted array
        arr = [1, 5, 3, 2, 4, 7, 8, 6, 9]
        sut = arr_to_bst(arr)

        self.assertEqual(sut.root.data, 5)
        self.assertEqual(sut.root.left.data, 3)
        self.assertEqual(sut.root.left.right.data, 4)

    def test_true(self):
        self.assertEqual(True, True)
