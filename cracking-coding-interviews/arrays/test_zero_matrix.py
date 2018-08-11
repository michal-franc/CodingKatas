import unittest

# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def rotate(matrix):

    n = len(matrix)
    m = len(matrix[0])

    row_mask = [False for x in range(n)]
    column_mask = [False for x in range(m)]

    # remember zeros in the initial array
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 0:
                row_mask[x] = True
                column_mask[x] = True

    for x in range(n):
        if row_mask[x]:
            for i in range(m):
                matrix[x][i] = 0

    for x in range(m):
        if column_mask[x]:
            for i in range(n):
                matrix[i][x] = 0

    return matrix

class SimpleTest(unittest.TestCase):
    def test_3x3(self):
        test_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected_result = [[1, 0, 1], [0, 0, 0], [1 ,0, 1]]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)

    def test_3x2(self):
        test_matrix = [[0, 1], [1, 1], [1, 1]]
        expected_result = [[0, 0], [0, 1], [0 ,1]]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)

    def test_2x2(self):
        test_matrix = [[0, 1], [1, 1]]
        expected_result = [[0, 0], [0, 1]]

        actual_result = rotate(test_matrix)

        self.assertEqual(actual_result, expected_result)
