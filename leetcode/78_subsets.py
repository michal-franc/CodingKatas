from simple_unittest import test
# TODO: remove duplicates

# using DP - iterative
# for each num in the nums
# add it to every subset inside the result
# and combine
# start [] 
# [] + [1] [],[1]
# [],[1] + [2] [1, 2]
def iterative(nums):
    nums.sort()
    result = [[]]

    for num in nums:
        result += [i + [num] for i in result] 

    return result

# using backtrack
def backtrack(result, subset, nums, start_index):

    result.append(list(subset))

    for i in range(start_index, len(nums)):
        # on i = 0
        # subset here is [1]
        subset.append(nums[i])

        # we hit another level of recurssion that starts from i = 1
        # which will lead to [2] added to [1] => [1, 2]
        # on next level for i = 2 we will add [3] to this mix getting [1, 2, 3]
        # all of these are added to the result as separate record
        backtrack(result, subset, nums, i + 1)

        # this is the actual backtrack step
        # we remove last element in case of [1, 2, 3] it becomes [1, 2]
        subset.pop()

    return result

def subsets(nums):
    return backtrack([], [], nums, 0)
    #return iterative(nums)

print subsets([1, 2, 3])
