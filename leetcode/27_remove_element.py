from simple_unittest import test

# Links:
# https://stackoverflow.com/a/19441944
# on pop, len computational expensiveness

# idea
# take index_left and index_right
# go with left till you hit val
# then go with right till you hit not val poping stuff
# swap left right - pop right
# repeat

# O(1) without additional mem
def removeElement(nums, val):

    if len(nums) <= 0:
        return 0

    index_right = len(nums) - 1
    index_left = 0

    while index_left <= index_right:

        if nums[index_left] != val:
            index_left += 1
        elif nums[index_right] == val:
            index_right -= 1
            nums.pop()
        else:
            nums[index_left], nums[index_right] = nums[index_right], nums[index_left]
            nums.pop()
            index_right -= 1
            index_left += 1

    return len(nums)

array = []
val = 0
expected_array = []
expected_len = 0
test('1. if nums empty then empty', removeElement(array, val), expected_len)
test('array ', array, expected_array) 

array = [1, 2]
val = 2
expected_array = [1]
expected_len = 1
test('2. if nums empty then empty', removeElement(array, val), expected_len)
test('array ', array, expected_array) 

array = [1, 2, 3]
val = 2
expected_array = [1, 3]
expected_len = 2
test('3. if nums empty then empty', removeElement(array, val), expected_len)
test('array ', array, expected_array) 

array = [3, 2, 2, 3]
val = 3
expected_array = [2, 2]
expected_len = 2
test('4. if nums empty then empty', removeElement(array, val), expected_len)
test('array ', array, expected_array) 

array = [0, 4, 4, 0, 4, 4, 4, 0, 2]
val = 4
expected_array = [0, 2, 0, 0]
expected_len = 4
test('5. if nums empty then empty', removeElement(array, val), expected_len)
test('array ', array, expected_array) 
