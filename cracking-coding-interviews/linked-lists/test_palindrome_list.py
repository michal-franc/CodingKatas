import unittest
from node import generate_node_list, generate_list_node, Node, print_list

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

def is_palindrome(list_start):
    reversed_list = reverse_list_with_clone(list_start)
    return compare_lists(reversed_list, list_start)

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
