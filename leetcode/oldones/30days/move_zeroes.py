from simple_unittest import test


# idea will be simple
# count number of zeroes and move non zero integers by this number to the left
# and put zero in the value if you move it
def moveZeroes(nums):
    numZeroes = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            numZeroes += 1
        elif numZeroes > 0:
            nums[i - numZeroes] = nums[i]
            nums[i] = 0

    return nums


test('leetcode example', moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
