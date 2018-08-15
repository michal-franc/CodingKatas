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

# using recursive unwinding
# this is O(n)
# Example:
# [1, 2, 3, 4] : k -> 2
# 1 -> 2 -> 3 -> 4 
# Node(2) <- (4, Node(2) <-(3, Node(2) <- (2, Node(2)) <- (1, None) <- (0, None) <- (-1, None)
def rec_call_unwinding(node, kth):

    if node is None:
        return (-1, None)

    (index, xth_node) = rec_call_unwinding(node.next, kth)
    index += 1

    # only set the 2nd value of tuple if kth hit
    if index == kth:
        return (index, node)

    # push the 2nd value with the kth elemtn up the stack 
    return (index, xth_node)

# iterative window
# this is O(n) and space O(1)
def iterative_window(node, kth):

    start = node
    end = node
    
    # this one creates a window of [start, 2, 3, 4, end], 6, 7, 8, 9
    for i in range(kth + 1):
        if end is None:
            return None
        end = end.next

    # moves window unitl end is None 
    # [start, 2, 3, 4, end], 6, 7, 8, 9
    # 1, [start, 3, 4, 5, end], 7, 8, 9
    # 1, 2, [start, 4, 5, 6, end], 8, 9
    # 1, 2, 3, [start, 5, 6, 7, end], 9
    # 1, 2, 3, 4, [start, 6, 7, 8, end]
    while end is not None:
        start = start.next
        end = end.next

    # 1, 2, 3, 4, [start, 6, 7, 8, end]
    # return start
    return start

def solution(start_node, kth):
    node = iterative_window(start_node, kth)
    return node

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
