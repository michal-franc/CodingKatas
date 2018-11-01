from simple_unittest import test

def flatten(array):

    result = []

    for i in array:
        if isinstance(i, int):
            result.append(i)
        else:
            result.extend(flatten(i))

    return result

test('[0, [1, [2, [3]]]]', flatten([0, [1, [2, [3]]]]), [0, 1, 2, 3])
test('[0]', flatten([0]), [0])
test('[[1,1], 0, [1, 1]]', flatten([[1, 1], 0, [1, 1]]), [1, 1, 0, 1, 1])
