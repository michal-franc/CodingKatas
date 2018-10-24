from binarytree import tree, bst, Node

def is_tree_perfect(tree_root):

    if root is None:
        return True

    depths = []
    nodes = []

    # using 'stack' for dfs
    nodes.append((tree_root, 0))

    while len(nodes):

        node, depth = nodes.pop()

        # check if it is a leaf
        if node.left is None and node.right is None:
            if depth not in depths:
                depths.append(depth)

                if len(depths) == 2:
                    return abs(depths[0] - depths[1]) <= 1

                # more than 2 distint depths always assumes that there will be diff by 1
                # example : [0, 1, 2] = 2 - 0 > 1
                if len(depths) > 2:
                    return False
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))


    return True

print "Perfect Tree"
root = tree(height=4, is_perfect=True)
print root 
print is_tree_perfect(root)

print "Not Perfect Tree"

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.left = Node(5)
print root
print is_tree_perfect(root)

