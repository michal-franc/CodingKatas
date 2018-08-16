import unittest
from node import Node

def delete_middle(delete_node):

    # trying to delete last element
    if delete_node is None or delete_node.next is None:
        return False

    # copies over next node and removes it by pointing current node.next to next.next
    n = delete_node.next
    delete_node.val =  n.val
    delete_node.next = n.next

    return True

class DeleteMiddleTest(unittest.TestCase):
    def test_true(self):

        test_node = Node(3, Node(4, None))
        start_node = Node(1, Node(2, test_node))

        self.assertEqual(start_node.next.next.val, 3)

        delete_middle(test_node)

        self.assertEqual(start_node.next.next.val, 4)
        self.assertEqual(start_node.next.val, 2)
        self.assertEqual(start_node.val, 1)
