import unittest
from linked_list import Node, NodeList, LinkedList
from node import node_len

# This solution is O(n) as we dont need another loop to find previous Node
# space is O(n) due to the buf
def node_remove_dups(start_node):
    buf = {}

    current_node = start_node
    previous_node = None

    while current_node != None:
        buff_next = current_node.next
        if current_node.val in buf:
            previous_node.next = buff_next
            current_node.next = None
            current_node = buff_next
        else:
            buf[current_node.val] = True
            previous_node = current_node
            current_node = buff_next

    return start_node

class UsingNodeTest(unittest.TestCase):
    def test_double_1_duplicate(self):

        start_node = NodeList(1, NodeList(1, None))

        actual_list = node_remove_dups(start_node)

        self.assertEqual(1, node_len(actual_list))

    def test_double_2_duplicate(self):

        start_node = NodeList(1, NodeList(1, NodeList(1, None)))

        actual_list = node_remove_dups(start_node)

        self.assertEqual(1, node_len(actual_list))

    def test_one_node(self):

        start_node = NodeList(1, None)

        actual_list = node_remove_dups(start_node)

        self.assertEqual(1, node_len(actual_list))

    def test_more_complicated(self):

        start_node = NodeList(1, NodeList(2, NodeList(3, NodeList(4, NodeList(1, None)))))

        self.assertEqual(5, node_len(start_node))

        actual_list = node_remove_dups(start_node)

        self.assertEqual(4, node_len(actual_list))

# this solution is O(n^2)
# due to iterating through initial list 
# and looking for a parent that is also a lookup

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

class UsingLinkedListTest(unittest.TestCase):
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
