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

def generate_next(arr,  n):

    if len(arr) == 0:
        n.next = None
    else:
        next_node = Node(arr[0], None)
        n.next = next_node
        generate_next(arr[1:], next_node)

    return n

def generate_node_list(arr):
    start_node = Node(arr[0], None)
    return generate_next(arr[1:], start_node)

def generate_list_node(start_node):
    buf = []

    current_node = start_node

    while current_node != None:
        buf.append(current_node.val)
        current_node = current_node.next

    return buf

def print_list(start_node):

    buf = []

    current_node = start_node

    while current_node != None:
        buf.append("%i -> " % current_node.val)
        current_node = current_node.next

    return ''.join(buf)
