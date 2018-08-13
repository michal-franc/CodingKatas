import unittest

class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList(object):
    def __init__(self, start_node):
        self.start_node = start_node
        self.last_node = start_node
        self.length = 1

    def add(self, new_node):
        self.last_node.next = new_node
        self.last_node = new_node
        self.length += 1

    def remove(self, current_node):

        parent_node = self.find_parent(current_node)

        if current_node.next is None:
            self.last_node = parent_node

        parent_node.next = current_node.next
        current_node.next = None

        self.length -= 1

    def find_parent(self, node):
        parent = self.start_node

        while parent.next != node:
            parent = parent.next

        return parent

class SimpleTest(unittest.TestCase):
    def test_simple_linked_list(self):
        linked_list = LinkedList(Node(1))
        linked_list.add(Node(2))
        linked_list.add(Node(3))

        self.assertEqual(3, linked_list.length)
        self.assertEqual(1, linked_list.start_node.val)
        self.assertEqual(3, linked_list.last_node.val)

    def test_find_parent_node(self):
        parent_node = Node(1)
        test_node = Node(2)

        linked_list = LinkedList(parent_node)
        linked_list.add(test_node)
        linked_list.add(Node(3))

        found_parent = linked_list.find_parent(test_node)

        self.assertEqual(3, linked_list.length)
        self.assertEqual(found_parent, parent_node)

    def test_remove(self):
        test_node = Node(2)
        last_node = Node(3)

        linked_list = LinkedList(Node(1))
        linked_list.add(test_node)
        linked_list.add(last_node)

        linked_list.remove(test_node)

        self.assertEqual(2, linked_list.length)
        self.assertEquals(linked_list.start_node.next.next, None)
        self.assertEquals(linked_list.last_node, last_node)

    def test_remove_end(self):
        prev_node = Node(2)
        last_node = Node(3)

        linked_list = LinkedList(Node(1))
        linked_list.add(prev_node)
        linked_list.add(last_node)

        linked_list.remove(last_node)

        self.assertEqual(2, linked_list.length)
        self.assertEquals(linked_list.last_node, prev_node)
        self.assertEquals(linked_list.start_node.next.next, None)
