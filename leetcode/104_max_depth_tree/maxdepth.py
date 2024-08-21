class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def traverse(root, level):

            if root == None:
                return ""

            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)

        return str.rstrip(traverse(self, 0))

    def __eq__(self, other):

        if not self and not other:
            return True

        if not self or not other:
            return False

        if self.val != other.val:
            return False

        return self.left == other.left and self.right == other.right
        

def buildTree(arr, index):
    if index >= len(arr):
        return None
    
    node = TreeNode(arr[index])
    node.left = buildTree(arr, 2 * index + 1)
    node.right = buildTree(arr, 2 * index + 2)
    return node

def createTreeFromArray(arr):
    if not arr:
        return None

    return buildTree(arr, 0)


def maxDepth(tree, currentDepth):

    if tree == None:
        return currentDepth

    return max(maxDepth(tree.left, currentDepth + 1), maxDepth(tree.right, currentDepth + 1))
