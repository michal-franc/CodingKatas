from binarytree import tree, bst, Node

# remember its not binary search tree

# pre order [root, [root1, [child1], [child1]], [root2, [child2], [child2]]
# where child is another subtree
# in order = [[child1], root1, [child1]], root, [[child2], root2, [child2]]]
def rec_build_tree(root, preorder, inorder):

    # wee look for the root value in inorder to find the 'median' point
    median_point = inorder.index(preorder[0])

    # based on the location of root value in inorder 
    # we can divide the arrays for left subtree and right subtree
    # and recurseively divide and conquer the problem
    left_preorder = preorder[1:median_point + 1]
    left_inorder = inorder[:median_point]

    right_preorder = preorder[median_point + 1:]
    right_inorder = inorder[median_point + 1:]

    if len(left_preorder) > 0:
        root.left = Node(left_preorder[0])
        rec_build_tree(root.left, left_preorder, left_inorder)

    if len(right_preorder) > 0:
        root.right = Node(right_preorder[0])
        rec_build_tree(root.right, right_preorder, right_inorder)

    return root

def build_tree(preorder, inorder):

    if len(preorder) <= 0:
        return []

    # with pre order we can always assume that first element is the root
    # root = preorder[0]
    root_value = preorder[0]
    root = Node(root_value)
    return rec_build_tree(root, preorder, inorder)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print build_tree(preorder, inorder)
