from simple_unittest import test
# are coordinates ordered?
# assume for now yes

# Tangens of angle should always be equal a/b in triangle

def checkStraightLine(coordinates):
    if len(coordinates) <= 1:
        return None

    if len(coordinates) == 2:
        return True

    # check first and last point what is the diff in x and y
    first = coordinates[0]
    tangens = -1

    for point in coordinates[1:]:
        a = abs(first[0] - point[0])
        b = abs(first[1] - point[1])
        tangensNext = 0

        # line with one of the cords same doesnt have angle
        if a == 0 or b == 0:
            tangensNext = 0
        else:
            tangensNext = a/b

        if tangens == -1:
            tangens = tangensNext
        elif tangens != tangensNext:
            return False

    return True

test('If one point its not a Line', checkStraightLine([[1,2]]), None)
test('2 points is always straight', checkStraightLine([[1,2],[99,99]]), True)
test('leetcode true example', checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)
test('leetcode false example', checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)
test('true leetcode', checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]), True)