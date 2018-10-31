from simple_unittest import test
from binarytree import tree, bst, heap, Node

# inorder depth traversal of bst returns sorted array
def is_bst_valid_inorder_rec(root, array):

    if root.left:
        is_bst_valid_inorder_rec(root.left, array)

    array.append(root.value)

    if root.right:
        is_bst_valid_inorder_rec(root.right, array)

    return array


def is_bst_valid_inorder(root):

    array = is_bst_valid_inorder_rec(root, [])

    previous = float('-inf')
    for i in array:
        if i < previous:
            return False
        else:
            previous = i
    
    return True

def is_bst_valid_rec(root, min_val, max_val):

    if root is None:
        return True
    
    print(root.value)
    print(" %s" % min_val)
    print(" %s" % max_val)

    if root.value < min_val or root.value > max_val:
        return False

    return is_bst_valid_rec(root.left, min_val, root.value) and is_bst_valid_rec(root.right, root.value, max_val)
    
def is_bst_valid(root):
    #return is_bst_valid_rec(root, float('-inf'), float('inf'))
    return is_bst_valid_inorder(root)


bst_tree = bst(height=3)
print(bst_tree)
test('valid_bst', is_bst_valid(bst_tree), True)

non_bst = tree(height=3)
print(non_bst)
test('invalid bst - simple', is_bst_valid(non_bst), False)

non_bst_complex = Node(4)

non_bst_complex.left = Node(2)
non_bst_complex.left.left = Node(1)
non_bst_complex.left.right = Node(3)
non_bst_complex.left.right.left = Node(1)
#non_bst_complex.left.right.right = Node(6)

non_bst_complex.right = Node(5)

print(non_bst_complex)
test('invalid bst - more complex', is_bst_valid(non_bst_complex), False)
