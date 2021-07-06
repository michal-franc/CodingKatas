from simple_unittest  import test

# time - O(n)
# space - O(1)
def move_zeroes(array):

    if len(array) <= 0:
        return []

    counter = 0
    for x in range(len(array)):
        if array[x] != 0:
            array[counter] = array[x]
            counter += 1

    while counter < len(array):
        array[counter] = 0
        counter += 1

test('basic', move_zeroes([]), [])
test('basic', move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
test('basic', move_zeroes([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
test('basic', move_zeroes([0, 0, 0, 0, 1]), [1, 0, 0, 0, 0])
test('basic', move_zeroes([1, 0, 0, 0, 1]), [1, 1, 0, 0, 0])
test('basic', move_zeroes([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
test('basic', move_zeroes([0, 0, 1, 1, 1]), [1, 1, 1, 0, 0])
test('basic', move_zeroes([0, 1, 0]), [1, 0, 0])
test('basic', move_zeroes([1, 0, 1, 0, 1]), [1, 1, 1, 0, 0])
test('basic', move_zeroes([1, 0, 2, 0, 3, 0, 4, 0, 0, 5]), [1, 2, 3, 4, 5, 0, 0, 0, 0 ,0])
