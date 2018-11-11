from simple_unittest import test
#Input: [3,2,1,0,4]
#Output: false
#Explanation: You will always arrive at index 3 no matter what. Its maximum
#             jump length is 0, which makes it impossible to reach the last index.

def find_zeroes(numbers):

    zeroes = []

    for i, n in enumerate(numbers[:len(numbers) - 1]):
        if n == 0:
            zeroes.append(i)

    return zeroes

def check_if_can_jump(zero_index, numbers):

    # this is special case as we dont have to jump past last index
    # so we need to set the needed jumps to 0 instead of 1
    if zero_index == len(numbers) - 1:
        need_to_jump = 0
    else:
        need_to_jump = 1

    for x in range(zero_index - 1, -1, -1):
        if numbers[x] > need_to_jump:
            return True

        # each element from zero we need more to jump
        need_to_jump += 1

    # we couldnt find element that could jump this zero
    return False



# the only possible way that we cannot make to the end 
# is if all the previous jumps reach to zero
# this is space O(1) - as we only keep last zero index in mem
# this is time O(n) + O(n) -> O(n)
def is_jump_game_possible(numbers):

    if len(numbers) <= 0:
        return True

    if len(numbers) == 1:
        return True

    # simple solution 
    # find if we can get past the zero's
    # find first zero in the array
    # and then check if index[zero] - 1 > 1
    # and then check if index[zero] - 2 > 2
    # this would have to be repeated for all the zero's

    # [0... impossible]
    # first jump is not possible
    if numbers[0] == 0:
        return False

    zeroes_index = find_zeroes(numbers)

    if len(zeroes_index):
        # check all the previous elements in array until you hit the end or zero
        for zero in zeroes_index:

            if check_if_can_jump(zero, numbers):
                continue
            else:
                return False

    # if no zeroes it is always possible
    else:
        return True

    return True

test('first zero', is_jump_game_possible([0, 1, 2, 3, 4, 5]), False)
test('no zero', is_jump_game_possible([1, 2, 3, 4, 5]), True)
test('zero', is_jump_game_possible([3, 2, 1, 0, 4]), False)
test('zero at the end', is_jump_game_possible([3, 2, 1, 0]), True)
test('zero at the end but possible', is_jump_game_possible([10, 2, 1, 0]), True)
test('empty', is_jump_game_possible([]), True)
test('possible', is_jump_game_possible([2, 0, 0]), True)
test('possible', is_jump_game_possible([1, 0, 1, 0]), False)
test('impossible', is_jump_game_possible([1, 0, 0, 1, 1, 2, 2, 0, 2, 2]), False)
test('impossible', is_jump_game_possible([2, 0, 1, 0, 1]), False)
