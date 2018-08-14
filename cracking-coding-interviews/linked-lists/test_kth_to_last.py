from node import node_len, Node
import unittest

# looping through the list kth to last 2 to last 
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 2nd to last -> 4

# this is a solutin with O(n) - brute force
# get the length of list O(n) -> or if we would have linkedlist with maintaned lenght counter this would be O(1)
# loop throught with counter and return node if counter hits len - kth - O(n)
# O(n) + O(n) -> O(n)
# Space O(1)
def brute_force(start_node, kth):
    length = node_len(start_node) # O(n)

    if length - kth <= 0:
        return None

    counter = 0 
    current_node = start_node

    while current_node != None:
        counter += 1 
        if counter >= length - kth:
            return current_node
        current_node = current_node.next

    return None

# loop throught the list with - O(n)
# pop the stack with O(n)
# O(n) + O(n) -> O(n)
# Space O(n)
def using_stack(start_node, kth):

    stack = []

    current_node = start_node

    while current_node != None:
        stack.append(current_node)
        current_node = current_node.next

    if len(stack) - kth <= 0:
        return None

    for x in range(kth):
        stack.pop()

    return stack.pop()

def solution(start_node, kth):
    return using_stack(start_node, kth)

class KthToLastTest(unittest.TestCase):
    def test_simple_test(self):

        start_node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))

        kth_node = solution(start_node, 2)

        self.assertEqual(kth_node.val, 4)

    def test_no_kth_element(self):

        start_node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))

        kth_node = solution(start_node, 8)

        self.assertEqual(kth_node, None)

    def test_1_element(self):

        start_node = Node(1, None)

        kth_node = solution(start_node, 0)

        self.assertEqual(kth_node, start_node)
