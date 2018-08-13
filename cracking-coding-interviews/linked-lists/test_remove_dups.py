import unittest
from linked_list import Node, LinkedList

def remove_dups(linked_list):
    buf = {}

    current_node = linked_list.start_node

    while current_node != None:
        buff_next = current_node.next
        if current_node.val in buf:
            linked_list.remove(current_node)
        else:
            buf[current_node.val] = True

        current_node = buff_next

    return linked_list

class SimpleTest(unittest.TestCase):
    def test_double_no_duplicate_2(self):

        test_list = LinkedList(Node(1))
        test_list.add(Node(2))

        actual_list = remove_dups(test_list)

        self.assertEqual(2, actual_list.length)

    def test_double_1_duplicate(self):

        test_list = LinkedList(Node(1))
        test_list.add(Node(1))

        actual_list = remove_dups(test_list)

        self.assertEqual(1, actual_list.length)

    def test_double_2_duplicate(self):

        test_list = LinkedList(Node(1))
        test_list.add(Node(1))
        test_list.add(Node(1))

        actual_list = remove_dups(test_list)

        self.assertEqual(1, actual_list.length)

    def test_double_3_duplicate(self):

        start_node = Node(2)
        test_node = Node(1)

        test_list = LinkedList(start_node)
        test_list.add(Node(2))
        test_list.add(test_node)
        test_list.add(Node(2))

        actual_list = remove_dups(test_list)

        self.assertEqual(2, actual_list.length)
        self.assertEqual(actual_list.start_node, start_node)
        self.assertEqual(actual_list.last_node, test_node)
        self.assertEqual(actual_list.start_node.next, test_node)
        self.assertEqual(actual_list.start_node.next.next, None)
        self.assertEqual(actual_list.last_node.next, None)
