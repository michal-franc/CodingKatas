from simple_unittest import test

def twoSum(nums, target):

    lookup_cache = {}

    for i, a in enumerate(nums):
        b = target - a
        if b in lookup_cache:
            return [lookup_cache[b], i]
        else:
            lookup_cache[a] = i

    return []

test('empty', twoSum([], 0), [])
test('one', twoSum([1, 1], 2), [0, 1])
test('[2, 7, 11, 15] -> 9', twoSum([2, 7, 11, 15, 9], 9), [0, 1])
test('[0, 1] -> 1', twoSum([0, 1], 1), [0, 1])
test('[7, 11, 15] -> 26', twoSum([7, 11, 15], 26), [1, 2])
