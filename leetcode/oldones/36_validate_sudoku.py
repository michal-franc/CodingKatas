# brute force:
# time complexity = O(n*m)
# space complexity = O(n) + O(m) + O(1)
def validate_sudoku(board):

    row = set()
    column = [set() for _ in xrange(len(board[0]))]
    boxes = [set() for _ in xrange(len(board[0]) / 3)]

    for y in range(len(board)):
        if y % 3 == 0:
            for box in boxes:
                box.clear()

        for x in range(len(board[0])):

            current_box = x / 3
            value = board[y][x]

            if value in column[x] or value in row:
                return False

            if value in boxes[current_box]:
                return False

            if value.isnumeric():
                column[x].add(value)
                row.add(value)
                boxes[current_box].add(value)

        row.clear()

    return True

test_input_small = [
  ["5","3","."],
  ["6",".","."],
  [".","9","8"]
]

#print(validate_sudoku(test_input_small))

test_input_valid = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

#print(validate_sudoku(test_input_valid))

test_input_invalid = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

#print(validate_sudoku(test_input_invalid))

test_invalid_one = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

print(validate_sudoku(test_invalid_one))


