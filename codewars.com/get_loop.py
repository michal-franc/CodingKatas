# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
from asyncore import loop
from simple_unittest  import test

def loop_size(node):
    visited = {node}
    nextNode = node

    # first loop to get out of the tail
    while True:
        nextNode = nextNode.next
        if nextNode in visited:
            break
        else:
            visited.add(nextNode)

    loop_size = 1
    visited = {nextNode}
    # second loop to get the loops size
    while True:
        nextNode = nextNode.next
        if nextNode in visited:
            break
        else:
            visited.add(nextNode)
            loop_size += 1
    
    return loop_size

