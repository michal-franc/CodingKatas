def findsum(array, target):
    for ix, x in enumerate(array):
        cut = ix+1
        for iy, y in enumerate(array[cut:]):
            if x + y == target:
                return [ix, iy+cut]

    return "cannot work"

def finditer(array, target):
    for x in range(len(array)):
        for y in range(x+1, len(array)):
            if array[x] + array[y] == target:
                return [x, y]

    return "cannot work"

def findhash(array, target):

    nums = {}

    for i, x in enumerate(array):
        nums[x] = i

    for i, x in enumerate(array):
        if target - x in nums and i != nums[target-x]:
                return [i, nums[target-x]]

    return "cannot work"

def findhashonepass(array, target):

    nums = {}

    for i, x in enumerate(array):
        nums[x] = i
        if target - x in nums and i != nums[target-x]:
            return [nums[target-x], i]

    return "cannot work"
