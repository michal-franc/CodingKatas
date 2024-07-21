from simple_unittest  import test

def scoreFlipMatrix(grid):

    maxSum = 0

    height = len(grid)
    width = len(grid[0])


    for i in range(height):
        row = grid[i]
        if row[0] != 1:
            grid = flipRow(i, grid)

    for x in range(width):
        zeros = 0
        ones = 0
        for y in range(height):
            if grid[y][x] == 0:
                zeros +=1
            else:
                ones +=1
            
        if zeros > ones:
            grid = flipCol(x, grid)

    for r in range(height):
        row = grid[r]
        string_ints = [str(int) for int in row]
        bin = int(''.join(string_ints), 2)
        maxSum += bin


    return maxSum


def flipCol(colNr, grid):
    for x in range(len(grid)):
       grid[x][colNr] = int(not grid[x][colNr]) 
    return grid

def flipRow(rowNr, grid):
    row = grid[rowNr]
    for i in range(len(row)):
        row[i] = int(not row[i])
    return grid

def printN(grid):
    for i in range(len(grid)):
        print(grid[i])


test('basic', scoreFlipMatrix([[0,0,1,1],[1,0,1,0],[1,1,0,0]]), 39)