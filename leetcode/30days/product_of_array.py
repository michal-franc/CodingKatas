from simple_unittest import test

# 1. first solution brute force
# for each element multiply the rest
# but this one has complexity O(n^2)

# Conditions
# no division and O(n)

def productOfArrayBruteForce(nums):

    result = [1] * len(nums)

    for i in range(len(nums)):
        for x in range(len(nums)):
            if x == i:
                continue
            result[i] *= nums[x]

    return result

# 2. with division
# 1 for to calculate total value by multiplying all
# 1 for to go through each element and divide by it
# remember about zeros as you cant divide by zero
# this gives O(2n)

def productOfArrayWithDivision(nums):
    result = [0] * len(nums)
    totalMultiplication = 1

    foundZeroIndex = -1
    foundMultipleZeroes = False

    for i, x in enumerate(nums):
        if x == 0:
            if foundZeroIndex != -1:
                foundMultipleZeroes = True
                break
            # if zero found then we just ahead and calculate multiplication without zero included
            foundZeroIndex = i
            continue

        totalMultiplication *= x

    # if multiple zeros found then we know that all the values are equal to zero
    if foundMultipleZeroes:
        return result

    if foundZeroIndex != -1:
        result[foundZeroIndex] = totalMultiplication
        return result

    for i, x in enumerate(nums):
        result[i] = totalMultiplication / x

    return result

# 3. without division
# product to the left and right and multiply them
def productOfArrayWithoutDivision(nums):
    l = len(nums)

    result, left, right = [0] * l, [0] * l, [0] * l

    left[0] = 1
    for i in range(1, l):
        left[i] = nums[i - 1] * left[i - 1]

    right[l - 1] = 1
    for i in reversed(range(l -1)):
        right[i] = nums[i + 1] * right[i + 1]

    for i in range(l):
        result[i] = left[i] * right[i]

    return result

test('leetcode example', productOfArrayWithoutDivision([1,2,3,4]), [24,12,8,6])
test('with negative value', productOfArrayWithoutDivision([-1,2,3,4]), [24,-12,-8,-6])
test('with 1 zero', productOfArrayWithoutDivision([0,2,3,4]), [24,0,0,0])
test('with 2 zeros', productOfArrayWithoutDivision([0,2,0,4]), [0,0,0,0])
