def twoSum(nums, target):
    # we can leverage the O(1) for hashmap to lookup keys existence
    cache = {}

    for i, x in enumerate(nums):
        b = target - x
        if b in cache:
            return [cache[b], i]
        else:
            cache[x] = i

    return []   
