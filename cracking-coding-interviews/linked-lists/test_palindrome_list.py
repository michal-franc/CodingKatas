import unittest
from node import generate_node_list, generate_list_node, Node, print_list, node_len

def compare_lists(one, two):
    current_one = one
    current_two = two

    while current_one is not None or current_two is not None:

        if current_one.val != current_two.val:
            return False

        current_one = current_one.next
        current_two = current_two.next

        if current_one is not None and current_two is None:
            return False

        if current_one is None and current_two is not None:
            return False

    return True

def reverse_list_with_clone(n):
    if n == []:
        return n

    end_node = Node(0, None)

    previous = None
    current = n

    while current is not None:
        end_node.val = current.val
        end_node.next = previous
        previous = end_node
        current = current.next
        end_node = Node(0, None)

    return previous

# First solution reverse linked list and check if they match
# then reverse is O(n) and compare is O(n) space is O(n) for new list buff

# We can also go down the recurrence path and when we reach the end we
# can start processing recurrence with the current list this will make
# space to be O(1)-if we dont count resources on the stack as part of space complexity

def is_palindrome_reverse_compare(list_start):
    reversed_list = reverse_list_with_clone(list_start)
    return compare_lists(reversed_list, list_start)

def is_palindrome_iterative_fast_slow(list_start):

    fast = list_start
    slow = list_start
    stack = []

    # for odd linked list -> 1 - 2 - 3 - 2 - 1
    # 1 - 2 - 3 - 2 - 1
    # slow
    # fast
    # 1 - 2 - 3 - 2 - 1
    #     slow
    #         fast
    # 1 - 2 - 3 - 2 - 1
    #         slow
    #                 fast
    # slow reached middle - fast is at the end

    # for even linked list -> 1 - 2 - 2 - 1
    # 1 - 2 - 2 - 1
    # slow
    # fast
    # 1 - 2 - 2 - 1
    #     slow
    #         fast
    # 1 - 2 - 2 - 1 - None
    #         slow
    #                 fast
    # slow reached middle - fast is None

    while fast is not None and fast.next is not None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    # for odd ignore middle element
    if fast is not None:
        slow = slow.next

    while slow is not None:
        elem = stack.pop()

        if elem != slow.val:
            return False

        slow = slow.next

    return True

# if we know length we can go down through the recursive path to the middle
# by doing length - 2 until we reach 0 or 1
def is_palindrome_recursive(head, length):
    # reaching the base case middle
    # 1 - 2 - 3 - 2 - 1
    #        base
    # even - as 0 is the last step
    if head is None or length <= 0:
        return (head, True)
    # odd - as -2 for odd should end on 1 -> next step would be -1
    elif length == 1:
        return (head.next, True)

    # go down the recurssion
    node, is_palin = is_palindrome_recursive(head.next, length - 2)

    # if in one of the steps we have found that values dont match
    # or one half of the the linked list is shorter
    # we assume that its not palindrome
    if is_palin is False or node is None:
        return (head, False)

    # check the value
    is_palin = head.val == node.val

    # move list on the left side to the next element
    node = node.next

    # move up the recurssion this will move head to the next element
    # 1 - 2 - 3 - 2 - 1
    #     h   b   n
    # 1 - 2 - 3 - 2 - 1
    # h               n 
    # even
    return (node, is_palin)

def is_palindrome(list_start):
    l = node_len(list_start)
    _, result = is_palindrome_recursive(list_start, l)
    return result

class FuncTest(unittest.TestCase):
    def test_reverse_list_one_element(self):
        test_list = generate_node_list([6])
        expected_list = generate_node_list([6])
        reversed_list = reverse_list_with_clone(test_list)

        self.assertEqual(True, compare_lists(expected_list, reversed_list))

    def test_reverse_list(self):
        test_list = generate_node_list([1, 2, 3, 4, 5, 6])
        expected_list = generate_node_list([6, 5, 4, 3, 2, 1])
        reversed_list = reverse_list_with_clone(test_list)

        self.assertEqual(True, compare_lists(expected_list, reversed_list))

    def test_basic_palindrome(self):

        test_list = generate_node_list([0, 1, 2, 1, 0])

        self.assertEqual(True, is_palindrome(test_list))

    def test_basic_not_palindrome(self):

        test_list = generate_node_list([0, 2, 2, 1, 0])

        self.assertEqual(False, is_palindrome(test_list))
