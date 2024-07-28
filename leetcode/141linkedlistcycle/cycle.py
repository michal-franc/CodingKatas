def hasCycle(head):
    # using toroise and hare algorithm

    if head == None or head.next == None:
        return False

    current = head
    current2 = head.next

    while current != None and current2 != None:
        current = current.next
        if current2.next == None or current2.next.next == None:
            return False

        current2 = current2.next.next

        if current == current2:
            return True

    return False
