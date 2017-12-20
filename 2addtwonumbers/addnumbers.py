class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def verifyNodes(values, l):
    if l != None and values == []:
        return "values size not match"

    if l == None and values != []:
        return "list size not match"

    if l == None and values == []:
        return True

    if values[0] != l.val:
        return "expected {0} but got {1}".format(values[0], l.val)

    return verifyNodes(values[1:], l.next)

def _carryVal(i1, i2):
    s = i1 + i2
    newVal = s % 10
    carry = s // 10

    return newVal, carry

def addTwoNumbers(l1, l2):

    if l1 == None:
        l1 = ListNode(0)

    if l2 == None:
        l2 = ListNode(0)

    newVal, carry = _carryVal(l1.val, l2.val)

    l1.val = newVal

    if carry > 0:
        if l1.next == None:
            l1.next = ListNode(carry)
            if l2.next == None:
                return l1
        else:
            l1.next.val = l1.next.val + carry 

    if l1.next == None and l2.next == None:
        return l1

    l1.next = addTwoNumbers(l1.next, l2.next)

    return l1
