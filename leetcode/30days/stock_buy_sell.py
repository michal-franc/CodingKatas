from simple_unittest import test

# check if each next element is higher or lower
# if its higher buy at x and then sell at next element get the profit

def buySellStock(nums):
    maxProfit = 0
    for i in range(len(nums)-1):
        if nums[i + 1] > nums[i]:
            maxProfit += nums[i + 1] - nums[i]

    return maxProfit

test('leetcode example', buySellStock([7,1,5,3,6,4]), 7)
test('leetcode example 1', buySellStock([1,2,3,4,5]), 4)
test('leetcode example 2', buySellStock([7,6,4,3,1]), 0)