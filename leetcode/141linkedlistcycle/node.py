class Node:
    next:'Node'

    def __init__(self, x = 0):
        self.val = x
        self.next = None

def createCyclicLinkedListFromArray(l, tailPointer=-1):
    current = None
    start = None
    cachedPointer = None

    counter = 0
    for x in l:
        if current == None:
            current = Node(x)
            start = current
            continue
        else:
            new = Node(x)
            current.next = new
            
            # remember the item which tail should point to
            if tailPointer != -1 and counter == tailPointer:
                cachedPointer = current

            current = new


        counter+=1

    if cachedPointer != None and current != None:
        current.next = cachedPointer

    return start

def createArrayFromLinkedList(listNode):

    l = [] 
    current = listNode

    while current != None:
        l.append(current.val)
        current = current.next

    return l

