import unittest
from node import Node, generate_node_list, print_list, generate_list_node

# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partition(start_node, pivot_value):

    head = start_node
    tail = start_node
    current_node = start_node

    while current_node is not None:
        nex = current_node.next
        if current_node.val < pivot_value:
            current_node.next = head
            head = current_node
        else:
            tail.next = current_node
            tail = current_node
        current_node = nex

    tail.next = None
    return head

class FuncTest(unittest.TestCase):
    def test_book(self):

        raw_list = [3, 5, 8, 5, 10, 2, 1]
        expected_list = [1, 2, 3, 5, 8, 5, 10]

        pivot = 5

        start_node = generate_node_list(raw_list)

        actual_node = partition(start_node, 5)
        
        print(print_list(start_node))
        print(print_list(actual_node))

        actual_list = generate_list_node(actual_node)

        self.assertEqual(expected_list, actual_list)

