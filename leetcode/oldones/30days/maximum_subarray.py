# https://afteracademy.com/blog/maximum-subarray-sum
# solutions

# first approach divide an conquer o(nlogn)
# second approach o(n)
import sys
from simple_unittest import test

# in this approach we use divide anc conquer recursivelly
# by doing calc maxSum on left, maxSum on right, maxSum on midpoint, check which one is higher
# will asume solution on slices to make it more clean

# crossoverr calculation
# starting fom the middle go each way and check max sum
# then sum them together and you will get max in crossover
# check for currentSum = 0 will take care of negative numbers
def biggestSumCrossOver(nums):
    midpoint = len(nums) // 2

    leftSum = -sys.maxint
    rightSum = -sys.maxint
    currentSum = 0

    # from midpoint -> 0
    for i in reversed(nums[0:midpoint]):
        currentSum += i
        if currentSum > leftSum:
            leftSum = currentSum

    # from midpoint -> last element
    for i in nums[midpoint:]:
        currentSum += i
        if currentSum > rightSum:
            rightSum = currentSum
    return leftSum + rightSum

def divideAndConquerSubArray(nums):
    if len(nums) == 1:
        return nums[0]

    midpoint = len(nums) // 2
    return max(divideAndConquerSubArray(nums[0:midpoint]),
               divideAndConquerSubArray(nums[midpoint:]),
               biggestSumCrossOver(nums))


# the idea is to go through each value lineary and if a sum reaches < 0 then we know 
# that this subarray will no longer produce max and we can start from 0
# [-2, 1, 2,-3, 4]
# 1 iteration - current sum -2 so we just assume that -2 could be the maxSum as its higher than max
# but we know that if next value is negative the sum will be smaller
# same if the next value is positive we can just assume that max sum will be equal this positive number
# so next iteratin we can start with 0 again
# 2 iteration - current sum 1 so we assume that its maxSum 1 so far and we move on to next value
# 3 iteration - curr sum 1 + 2 = 3 - nice the value was positrive so we know we are going in the right direction
# 4 irteration the value is 0 = cool nothing happened
# 5 iteration the value is 4 sum is 4 so maxSum is 4
def linearMaxSubArray(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    # has to be -maxint to prevent situation when maxSum is higher that value in nums
    # rost case value in nums is equal to -sys.maxint so then we can return -sys.maxint
    maxSum = -sys.maxint
    currentSum = 0

    for i in nums:
        currentSum += i
        if currentSum <= 0:
            maxSum = max(maxSum, i)
            currentSum = 0
        else:
            if maxSum < currentSum:
                maxSum = currentSum

    return maxSum


test('leetcode example', divideAndConquerSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
# with all minuses we just need to return lowest value in the array
test('leetcode all minuses', divideAndConquerSubArray([-2, -1, -3, -4, -1]), -1)
