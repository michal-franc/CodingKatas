import unittest
from node import Node, generate_node_list, print_list, generate_list_node

# first idea go through first list add nodes to hashtable
# with number of how many times it was visited O(n)
# go through second list do the same to hash and return 
# if you hit a key already existed this is the node you are looking for
# worst case this is O(n) assuming that intersetion is at the last nodeA
# to keep nodes we also need hash-table O(n) space
# time -> 2 * O(n)
# space -> O(n)

def intersection_first(list1, list2):
    hash_set = {}

    current = list1

    while current is not None:
        hash_set[current] = True
        current = current.next

    current = list2

    while current is not None:
        if current in hash_set:
            return current
        current = current.next

    return None

def intersection_first(list1, list2):
    hash_set = {}

    current = list1

    while current is not None:
        hash_set[current] = True
        current = current.next

    current = list2

    while current is not None:
        if current in hash_set:
            return current
        current = current.next

    return None

# There is a way to remove space requirement O(N) by moving to O(1)
# Traverse get the tails and lengths
# if tails dont match return False 
# check length difference and decide which list is shorter or longer 
# advance longer list by the length differenceA
# if both 'pointers' match return True
# This also gives a best case of O(A + B)

def get_len_with_tail(list_start):

    if list_start is None:
        return (0, None)

    # starts from one bec we are not iterating through whole list just to tail
    counter = 1

    current = list_start

    while current.next != None:
        current = current.next
        counter += 1

    return (counter, current)

def intersection_second(list1, list2):

    len_list1, tail_list1 = get_len_with_tail(list1)
    len_list2, tail_list2 = get_len_with_tail(list2)

    if tail_list1 is not tail_list2:
        return None

    len_diff = abs(len_list2 - len_list1)
    if len_list2 > len_list1:
        for _ in range(len_diff):
            list2 = list2.next

    if len_list1 > len_list2:
        for _ in range(len_diff):
            list1 = list1.next

    while list1 != None:

        if list1 is list2:
            return list1

        list1 = list1.next
        list2 = list2.next

    return None

def intersection(list1, list2):
    return intersection_second(list1, list2)

class FuncTest(unittest.TestCase):
    def test_intersection_no_intersection(self):
        self.assertEqual(None, intersection(Node(1, None), Node(1, None)))

    def test_intersection_one_none(self):
        self.assertEqual(None, intersection(Node(1, None), None))

    def test_intersection_both_empty(self):
        self.assertEqual(None, intersection(None, None))

    def test_intersection_basic(self):

        inter_node = Node(7, None)
        inter_node.val = Node(2, Node(1, None))
        inter_up = Node(9, inter_node)
        inter_down = Node(6, inter_node)

        list1 = Node(3, Node(1, Node(5, inter_up)))
        list2 = Node(4, Node(6, inter_down))

        self.assertEqual(inter_node, intersection(list1, list2))
