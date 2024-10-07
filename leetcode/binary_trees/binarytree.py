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
        

def buildTree(arr):
    if len(arr) == 0:
        return None

    nodes = []

    # using arr.pop(0) prevents us from using index i
    # but it modifies original array
    root = TreeNode(arr.pop(0))
    nodes.append(root)

    while len(arr) > 0:
        curr = nodes.pop(0)

        left_val = arr.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(arr) > 0:
            right_val = arr.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

    return root

def createTreeFromArray(arr):
    if not arr:
        return None

    return buildTree(arr)

