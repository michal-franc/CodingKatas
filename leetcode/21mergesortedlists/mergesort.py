class ListNode:
    next:'ListNode'

    def __init__(self, x = 0):
        self.val = x
        self.next = None

def listNodeHelper(l):

    current = None
    start = None

    for x in l:
        if current == None:
            current = ListNode(x)
            start = current
        else:
            new = ListNode(x)
            current.next = new
            current = new

    return start

def listNodeToList(listNode):

    l = [] 
    current = listNode

    while current != None:
        l.append(current.val)
        current = current.next

    return l

def merge(list1, list2):
    iter1, iter2 = list1, list2
    current = None
    start = None
    while iter1 != None or iter2 != None:

        value = 0
        if iter1 != None and iter2 != None:
            if iter1.val < iter2.val:
                value = iter1.val
                iter1 = iter1.next
            else:
                value = iter2.val
                iter2 = iter2.next
        elif iter1 != None:
            value = iter1.val
            iter1 = iter1.next
        elif iter2 != None:
            value = iter2.val
            iter2 = iter2.next

        if current == None:
            current = ListNode(value)
            start = current
        else:
            current.next = ListNode(value)
            current = current.next

    return start
