class Node(object):
    def __init__(self, val, n):
        self.next = n
        self.val = val

def node_len(start_node):

    len_counter = 0
    current_node = start_node

    while current_node != None:
        current_node = current_node.next
        len_counter += 1

    return len_counter
