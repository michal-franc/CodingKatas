# solutions
# super brute force - for each element search rest of list
# but this is O(n^2) as we repeat the list search for each element

# brute force - go through each item and count them to dict then go through dict and find items with 1 element
# this would give O(n) as this would be 
# pass through array O(n) + pass through dict O(n)

# but there is a solution without additional memory
# so we could modify existing input? by moving single digit to somewhere inside the original nums array
# the fact that it can either appar once or twice is significant
# how can we use twice?

# looked up on the net and you can use xor for it


from simple_unittest import test

def singleNumber(nums):

    result = 0

    if len(nums) == 0:
        return None

    for num in nums:
        result ^= num

    return result

test('2 2 1 -> 1', singleNumber([2, 2, 1]), 1)
test('4 1 2 1 2 -> 4', singleNumber([4, 1, 2, 1, 2]), 4)
test('empty', singleNumber([]), None)
