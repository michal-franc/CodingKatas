from simple_unittest import test

# it has to be O(log n)
# so to get log n in sorted array we can use quick search
# but in this case it will be difficult to find midpoint as it shifted
# we cant just assume that mid point is in the middle

# it is ascending so to find 

# 1. lests just do quick search
# 2. then mutate quick search to work on pivot based array
# - find pivot by checking gradient
# - if array is ascending then we go up from midpoint

# no duplicates
def findPivot(nums, start, end):
    # situation like base array is [0] in odd arrays
    if start == end:
        return start

    # check if this is shifted array
    # its only shifter if nums[start] > nums[end]
    midpoint = (end + start) / 2
    
    # just check if we accidentaly have found pivot already will also cover cases like [7,0]
    if nums[midpoint] > nums[midpoint + 1]:
        return midpoint + 1

    # just check if we accidentaly have found pivot already will also cover cases like [7,0]
    if nums[midpoint - 1] > nums[midpoint]:
        return midpoint

    # if mid is greater than start it means that pivot is to the left
    if nums[midpoint] > nums[start]:
        return findPivot(nums, midpoint, end)
    # otherwise pivot is to the right
    else:
        return findPivot(nums, start, midpoint)

test('find pivot 1', findPivot([4,5,6,7,0,1,2], 0, 7), 4)
test('find pivot 2', findPivot([4,5,6,7,8,0,1,2], 0, 8), 5)
test('find pivot 3', findPivot([2,1], 0, 1), 1)
test('find pivot 3', findPivot([5,1,3], 0, 2), 1)

def quickSearch(nums, start, end, target):
    # we didn't find the index
    if start == end:
        return -1

    if target == nums[start]:
        return start

    if target == nums[end]:
        return end

    # this is to cover situation where there is [3,1] left and none matched (2 elem array)
    if end - start == 1:
        return -1

    midpoint = (end + start) / 2

    if target == nums[midpoint]:
        return midpoint

    if target > nums[midpoint]:
        return quickSearch(nums, midpoint + 1, end, target)
    else:
        return quickSearch(nums, start, midpoint - 1, target)

def searchRotated(nums, target):

    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    end = len(nums) - 1
    start = 0

    # situation with shifted array
    # this can be done thanks to no duplicates
    if nums[start] > nums[end]:
        pivotPoint = findPivot(nums, start, end)

        # we actually find the target on pivot point
        if target == nums[pivotPoint]:
            return pivotPoint

        if target > nums[end]:
            return quickSearch(nums, start, pivotPoint-1, target)
        else:
            return quickSearch(nums, pivotPoint, end, target)

        return pivotPoint
    # otherwise just do normal quick search
    else:
        return quickSearch(nums, start, end, target)

test('test', searchRotated([5,1,3], 4), -1)
test('not found', searchRotated([0,1,2,3,4,5,6,7,8,9], 10), -1)
test('not found', searchRotated([0,1,2,3,4,5,6,7,8,9], -1), -1)
test('not shifted', searchRotated([0,1,2,3,4,5,6,7,8,9], 0), 0)

test('not shifted', searchRotated([0,1,2,3,4,5,6,7,8,9], 9), 9)
test('not shifted', searchRotated([8,9], 9), 1)

test('leetcode example shifted missing', searchRotated([4,5,6,7,0,1,2], 9), -1)
test('leetcode example shifted', searchRotated([4,5,6,7,0,1,2], 7), 3)
test('not shifted', searchRotated([8,9], 8), 0)
test('not shifted', searchRotated([3,1], 0), -1)
test('not shifted', searchRotated([3,1], 3), 0)
test('not shifted', searchRotated([1,3], 0), -1)
test('leetcode example shifted', searchRotated([4,5,6,7,0,1,2], 5), 1)