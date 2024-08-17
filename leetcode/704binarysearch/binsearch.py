def binSearch(array, target):
    # find middle
    left = 0
    right = len(array) - 1

    while left <= right:
        pivot = (right + left) // 2

        if(array[pivot] == target):
            return pivot

        if array[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return -1

