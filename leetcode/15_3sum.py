from simple_unittest import test

# sorted array and indexes
# time O(n^2)
# space O(1)

def threeSum_sorted(nums, length):

    # sorted array with left and right index trying to 'match sum'
    sorted_nums = sorted(nums)
    result = []

    for i in range(0, length - 2):
        left = i + 1
        right = length - 1

        while left < right:

            a = sorted_nums[i]
            b = sorted_nums[left]
            c = sorted_nums[right]

            if a + b + c == 0:
                left += 1
                right -= 1
                result.append([a, b, c])
            elif a + b + c < 0:
                left += 1
            elif a + b + c > 0:
                right -= 1

    return result

# time O(n^2)
# space O(n)
# c == -(a+b)

def threeSum_hash(nums, length):
    c_hash = {}

    for c_i in range(2, length - 1):
        c_hash[nums[c_i]] = True

    result = []
    for a_i in range(0, length - 2):
        for b_i in range(a_i + 1, length - 1):
            a = nums[a_i]
            b = nums[b_i]

            if -(a + b) in c_hash:
                result.append([a, b, -(a + b)])

    return result

# the brute force approach we can try goes through every element 3x for loop
# time O(n^3)
# space O(1)
def threeSum_brute(nums, length):
    result = []

    # to remove duplicates we start from 0 to -2
    for a_i in range(0, length - 2):
        # to remove duplicates we start from 1 to -1
        for b_i in range(a_i + 1, length - 1):
            # to remove duplicates we start from 2 to n
            for c_i in range(b_i + 1, length): 

                a = nums[a_i]
                b = nums[b_i]
                c = nums[c_i]
                
                if a + b + c == 0:
                    result.append([a, b, c])

    return result

def threeSum(nums):
    length = len(nums)

    if length < 3:
        return []

    return threeSum_sorted(nums, length)

test('two elements', threeSum([1, 2]), [])
test('empty', threeSum([]), [])
print threeSum([-1, 0, 1, 2, -1, -4])
