class ListNode:
    def __init__(self, x = 0):
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

def _calculateDigit(i1, i2):
    sum = i1 + i2
    newDigit= sum % 10
    carry = sum // 10

    return newDigit, carry

def addTwoNumbers(l1, l2):

    "add digit if matching missing for l1 or l2"
    if l1 == None:
        l1 = ListNode()

    if l2 == None:
        l2 = ListNode()

    newDigit, carry = _calculateDigit(l1.val, l2.val)

    l1.val = newDigit

    if carry > 0:
        "create new digit and initilize it"
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
