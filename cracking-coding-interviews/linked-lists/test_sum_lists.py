import unittest
from node import generate_node_list,generate_list_node,Node, print_list, node_len

# -----------------------------------------------------------------------
# first idea: go through each list and create number then use +
# O(N) + O(N) - 2*O(N)time
# two arrays for numbers - 2*O(N) -> space
# I can get rid of arrays if i have linked list and lenght maintaned ( so that dont have to do O(n) to get the len
# with len you can easilly calculate what is the base 10 for next and current value
# eg x * 10^0 -> x * 10^1 -> x * 10^2 
# then you can just have O(1) value to hold the number and use '+' operator
# -----------------------------------------------------------------------
# second idea:
# -----------------------------------------------------------------------
# we go step by step through each element sum the values to one of the exisitng lists
# we have to control carry over if sum is > 10
# after O(N) we should have a list with summed values
# then we need to go through O(N) and sum the values 
# of we maintain O(1) space value and add sum to it
# we can also simplify and maintaing O(N) space buff of digits and then just create string number and change it to int

def sum_lists_small_to_big(first_list_start, second_list_start):

    first_current = first_list_start
    second_current = second_list_start
    carry = 0
    base_10 = 0
    result = 0

    while first_current is not None or second_current is not None:

        current_val = 0
        if first_current is not None:
            current_val += first_current.val
            first_current = first_current.next

        if second_current is not None:
            current_val += second_current.val
            second_current = second_current.next

        current_val += carry

        carry = int(current_val/10)
        current_val = current_val % 10

        result += current_val * pow(10, base_10)
        base_10 += 1

    if carry != 0:
        result += carry * pow(10, base_10)

    return result

def pad_with_zero(node, how_many):

    for x in range(how_many):
        new_node = Node(0, node)
        node = new_node

    return node

def recurrence_sum(n1, n2):

    # we have reached the end so set the carry to zero and return zero sum
    if n1 is None and n2 is None:
        return Node(0, None)

    result_node = recurrence_sum(n1.next, n2.next)

    current_val = result_node.val
    current_val += n1.val
    current_val += n2.val

    carry = int(current_val / 10)
    current_val = current_val % 10

    result_node.val = current_val

    return Node(carry, result_node)

# recurrence is usefull in this example as it transform the problem to the previous one 
# summing from lowest to biggest -> which is cool
def sum_lists_big_to_small(first_list_start, second_list_start):

    first_len = node_len(first_list_start)
    second_len = node_len(second_list_start)

    # this will be used to shift the smaller one
    difference_len = abs(first_len - second_len)

    if first_len > second_len:
        second_list_start = pad_with_zero(second_list_start, difference_len)
    else:
        first_list_start = pad_with_zero(first_list_start, difference_len)

    result_list = recurrence_sum(first_list_start, second_list_start)

    # due to recurence sum imperfection if first elem is 0 then discard it and shift to next
    if result_list.val == 0:
        result_list = result_list.next

    return result_list

def sum_lists(first_list_start, second_list_start):
    return sum_lists_small_to_big(first_list_start, second_list_start)

class FuncListBigToSmall(unittest.TestCase):
    def test_same_length(self):

        first_list = generate_node_list([6, 1, 7])
        second_list = generate_node_list([2, 9, 5])

        expected_list  = [9, 1, 2] 
        actual_list  = generate_list_node(sum_lists_big_to_small(first_list, second_list))

        self.assertEqual(actual_list, expected_list)

    def test_diff_length(self):

        first_list = generate_node_list([1, 6, 1, 7])
        second_list = generate_node_list([2, 9, 5])

        expected_list  = [1, 9, 1, 2] 
        actual_list  = generate_list_node(sum_lists_big_to_small(first_list, second_list))

        self.assertEqual(actual_list, expected_list)

    def test_lots_of_carry(self):

        first_list = generate_node_list([9, 9, 9, 9])
        second_list = generate_node_list([9, 9, 9])

        expected_list  = [1, 0, 9, 9, 8] 
        actual_list  = generate_list_node(sum_lists_big_to_small(first_list, second_list))

        self.assertEqual(actual_list, expected_list)


class FuncTest(unittest.TestCase):
    def test_same_length(self):

        first_list = generate_node_list([7, 1, 6])
        second_list = generate_node_list([5, 9, 2])

        expected_sum = 912
        actual_sum = sum_lists(first_list, second_list)

        self.assertEqual(expected_sum, actual_sum)

    def test_diff_length(self):

        first_list = generate_node_list([7, 1, 6, 1])
        second_list = generate_node_list([5, 9, 2])

        expected_sum = 1912
        actual_sum = sum_lists(first_list, second_list)

        self.assertEqual(expected_sum, actual_sum)

    def test_lots_of_carry(self):

        first_list = generate_node_list([9, 9, 9, 9])
        second_list = generate_node_list([9, 9, 9])

        expected_sum = 10998
        actual_sum = sum_lists(first_list, second_list)

        self.assertEqual(expected_sum, actual_sum)

    def test_one_empty(self):

        first_list = generate_node_list([9, 9, 9, 9])
        second_list = None

        expected_sum = 9999
        actual_sum = sum_lists(first_list, second_list)

        self.assertEqual(expected_sum, actual_sum)
