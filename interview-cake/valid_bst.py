from binarytree import tree, bst, Node

def is_bst(root):

    # bst if on each level every left is smaller than parent and every right is bigger than parent
    # going to use bfs

    # using array as queue to do bfs
    nodes = []

    # base case
    nodes.append((root, -float('inf'), float('inf')))

    while len(nodes):

        node, lower_val, upper_val = nodes.pop(0)
    
        if node.value >= upper_val or node.value <= lower_val:
            return False

        if node.left:
            nodes.append((node.left, lower_val, node.value))

        if node.right:
            nodes.append((node.right, node.value, upper_val))

    return True

print "Not Bst"
root = tree(height=3)
print root 
print is_bst(root)

print "Bst"
root = bst(height=3)
print root
print is_bst(root)
