from simple_unittest import test

# we can go O(n) through list and put them in hash
# so that if x is counted then in hash there should be key x+1
# this gives us O(1) check if key exists

def countingElements(nums):
    mappedValues = {}
    counter = 0

    # O(n) to put values into map
    for n in nums:
        mappedValues[n] = True

    # O(n) to check if n+1 exists
    for n in nums:
        if n+1 in mappedValues:
            counter+=1

    # in the end its O(n)
    return counter

test('leetcode example', countingElements([1,2,3]), 2)
test('leetcode example1', countingElements([1,1,3,3,5,5,7,7]), 0)
test('leetcode example2', countingElements([1,3,2,3,5,0]), 3)
test('leetcode example3', countingElements([1,1,2,2]), 2)
test('leetcode example3', countingElements([1,1,1,2,2]), 3)