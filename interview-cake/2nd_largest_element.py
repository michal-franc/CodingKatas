from binarytree import tree, bst, Node

# basic assumption - largest items in bst are to the 'right'

def find_largest(root):
    current = root

    while current.right:
        current = current.right

    return current.value

def second_largest(root):

    parent = root
    current = root

    # find the largest element
    while current.right:
        parent = current
        current = current.right

    # check if there is a left element
    # if it is we have a subtree where we look for the largest element
    if current.left:
        return find_largest(current.left)
    else:
        # if right top most leaf doeasnt have left node
        # the 2nd largest is its parent
        return parent.value


root = bst(height=4)
print root
print second_largest(root)
