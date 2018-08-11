import unittest

# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_not_in_place(matrix):

    l = len(matrix)

    if l <= 1:
        return matrix

    result_matrix = [[''] * l for x in range(l)]

    for y in range(l -1, -1, -1):
        for x in range(l):
            result_matrix[abs(y - (l - 1))][x] = matrix[x][y]

    return result_matrix

def rotate(matrix):

    l = len(matrix)

    if l <= 1:
        return matrix

    # for l -> 3 there is no second layer so it stays inside

    for x in range(0, int(l/2)):
        for y in range(x, l-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][l-1-x]
            matrix[y][l-1-x] = matrix[l-1-x][l-1-y]
            matrix[l-1-x][l-1-y] = matrix[l-1-y][x]
            matrix[l-1-y][x] = temp

    return matrix

class SimpleTest(unittest.TestCase):
    def test_4x4(self):
        test_matrix = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['j', 'k', 'l', 'm'], ['o', 'p', 'r', 's']]
        expected_result = [['d', 'h', 'm', 's'], ['c', 'g', 'l', 'r'], ['b', 'f', 'k', 'p'], ['a', 'e', 'j', 'o']]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)

    def test_3x3(self):
        test_matrix = [['a', 'b'], ['c', 'd']]
        expected_result = [['b', 'd'], ['a', 'c']]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)

    def test_2x2(self):
        test_matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        expected_result = [['c', 'f', 'i'], ['b', 'e', 'h'], ['a', 'd', 'g']]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)

    def test_empty(self):
        test_matrix = []
        expected_result = []

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)

    def test_1by1(self):
        test_matrix = ["a"]
        expected_result = ["a"]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)
