# find where are the 0s
# keep list of coords of zeros in separate list as tuples
# move through each cord and 0 the elements in the array
def setZeroes_inplace(matrix):

    row_zero = False
    for y in range(len(matrix)):
        if matrix[y][0] == 0:
            row_zero = True

    col_zero = False
    for x in range(len(matrix[0])):
        if matrix[0][x] == 0:
            col_zero = True

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                matrix[y][0] = 0
                matrix[0][x] = 0

    for y in range(1, len(matrix)):
        if matrix[y][0] == 0:
            for x in range(1, len(matrix[0])):
                matrix[y][x] = 0
                
    for x in range(1, len(matrix[0])):
        if matrix[0][x] == 0:
            for y in range(1, len(matrix)):
                matrix[y][x] = 0

    if col_zero:
        for x in range(len(matrix[0])):
            matrix[0][x] = 0
    if row_zero:
        for y in range(len(matrix)):
            matrix[y][0] = 0
    

def setZeroes_1(matrix):
    x_bitmap = 0
    y_bitmap = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                # set bit x
                x_bitmap |= (1 << x)
                # set bit y
                y_bitmap |= (1 << y)

    for x in range(len(matrix[0])):
        # check bit x
        if x_bitmap & (1 << x):
            for _y in range(len(matrix)):
                matrix[_y][x] = 0 

    for y in range(len(matrix)):
        # check bit y
        if y_bitmap & (1 << y):
            for _x in range(len(matrix[0])):
                matrix[y][_x] = 0 

def setZeroes_nplusm(matrix):
    # O(n+m) space
    x_s = set()
    y_s = set()

    # O(n+m) time
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                x_s.add(x)
                y_s.add(y)

    #O(n*m)
    for x in x_s:
        for _y in range(len(matrix)):
            matrix[_y][x] = 0 

    #O(n*m)
    for y in y_s:
        for _x in range(len(matrix[0])):
            matrix[y][_x] = 0 

def setZeroes_nm(matrix):

    # O(n*m) space
    zeros = []

    # O(n*m) time
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                zeros.append((x, y))

    # O((n*m)*(n+m)) time - worst case we have matrix with only zeros
    for x, y in zeros:
        # x, y -> 0..n, x | y, 0..n
        for _x in range(len(matrix[0])):
            matrix[y][_x] = 0 

        for _y in range(len(matrix)):
            matrix[_y][x] = 0 


def setZeroes(matrix):

    setZeroes_inplace(matrix)

    for line in matrix:
        print line

setZeroes([[0, 1, 0],
           [1, 1, 1],
           [1, 1, 1]])

setZeroes([[1, 1],
           [1, 0],
           [1, 1]])

setZeroes([[1, 1, 1, 1],
           [1, 0, 1, 1],
           [1, 1, 1, 1]])


