import unittest
from node import Node, generate_node_list, print_list, generate_list_node

# using hash set of visited nodesa
# space: O(N)
# time: O(N)
def is_loop_hash(list_start):

    hash_set = {}

    current = list_start

    while current is not None:
        if current in hash_set:
            return current

        hash_set[current] = True
        current = current.next

    return None

# using fast - slow
# time: O(N)
# space: O(1)

# we use fast and slow till we hit the collistion 
# then we move slow back to start
# and move them at the same rate when they collide that is the loop start
# https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
def is_loop_fast_slow(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = head
    # if whole linked list is loop then this will alwasy be false
    # as the meeting point is the 'start' of the list
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast

def is_loop(list_start):
    return is_loop_fast_slow(list_start) 

class FuncTest(unittest.TestCase):
    def test_basic_test(self):

        e_node = Node('E', None)
        loop_node = Node('C', Node('D', e_node))
        e_node.next = loop_node
        list_start = Node('A', Node('B', loop_node))

        self.assertEqual('C', is_loop(list_start).val)
