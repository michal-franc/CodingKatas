import unittest
from addnumbers import ListNode, addTwoNumbers, verifyNodes

class SimpleTest(unittest.TestCase):
    def test_ListNodeLeetCode(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        l3 = addTwoNumbers(l1, l2)
        actual = verifyNodes([7, 0, 8], l3)

        self.assertEqual(actual, True)

    def test_ListNodeNoCarry(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(4)
        l2.next.next = ListNode(1)

        l3 = addTwoNumbers(l1, l2)
        actual = verifyNodes([7, 8, 4], l3)

        self.assertEqual(actual, True)

    def test_ListNodeCarryOver(self):
        l1 = ListNode(1)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        
        l3 = addTwoNumbers(l1, l2)
        actual = verifyNodes([6, 0, 8], l3)
 
        self.assertEqual(actual, True)

    def test_ListNodeNotSame(self):
        l1 = ListNode(1)
        l1.next = ListNode(4)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        
        l3 = addTwoNumbers(l1, l2)
        actual = verifyNodes([6, 0, 5], l3)
 
        self.assertEqual(actual, True)

    def test_LeetCode0(self):
        l1 = ListNode(1)
        l1.next = ListNode(8)

        l2 = ListNode(0)
        
        l3 = addTwoNumbers(l1, l2)
        actual = verifyNodes([1, 8], l3)
 
        self.assertEqual(actual, True)

    def test_ListNodeCarryOverNewNode(self):
        l1 = ListNode(1)
        l1.next = ListNode(4)
        l1.next.next = ListNode(6)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        
        l3 = addTwoNumbers(l1, l2)
        actual = verifyNodes([6, 0, 1, 1], l3)
 
        self.assertEqual(actual, True)

class VerifyNodesTest(unittest.TestCase):
    def test_valuesMores(self):
        l1 = ListNode(2)

        actual = verifyNodes([2, 1], l1)
        expected = "list size not match"

        self.assertEqual(actual, expected)

    def test_valuesLess(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)

        actual = verifyNodes([2], l1)
        expected = "values size not match"

        self.assertEqual(actual, expected)

    def test_properCheck(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)

        actual = verifyNodes([2, 4], l1)
        expected = True 

        self.assertEqual(actual, expected)

    def test_properCheckMore(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(4)
        l1.next.next.next = ListNode(9)

        actual = verifyNodes([2, 4, 4, 9], l1)
        expected = True 

        self.assertEqual(actual, expected)
