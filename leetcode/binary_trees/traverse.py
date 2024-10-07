from binarytree import TreeNode

# all are
# time O(n)
# space O(n)
def preOrder(root: TreeNode):
    if root == None:
        return []

    res = []

    def preOrderIn(root):
        if root == None:
            return

        nonlocal res

        res.append(root.val)
        preOrderIn(root.left)
        preOrderIn(root.right)

    preOrderIn(root)

    return res

def inOrder(root: TreeNode):
    if root == None:
        return []

    res = []

    def inOrderIn(root):
        if root == None:
            return

        nonlocal res

        inOrderIn(root.left)
        res.append(root.val)
        inOrderIn(root.right)

    inOrderIn(root)

    return res

def postOrder(root: TreeNode):
    if root == None:
        return []

    res = []

    def orderIn(root):
        if root == None:
            return

        nonlocal res

        orderIn(root.left)
        orderIn(root.right)
        res.append(root.val)

    orderIn(root)

    return res

def preOrderIterative(root: TreeNode):
    if root == None:
        return []

    res = []

    # it is simple using queue
    queue = [root]

    while len(queue) > 0:
        curr = queue.pop()
        res.append(curr.val)

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    return res

def levelOrder_rec(root: TreeNode):
    if root == None:
        return []

    levels = []

    def levelIn(node, level):
        if node == None:
            return

        if len(levels) <= level:
            levels.append([])

        levels[level].append(node.val)
        levelIn(node.left, level+1)
        levelIn(node.right, level+1)


    levelIn(root, 0)

    return levels

# iterative
def levelOrder(root: TreeNode):
    if root == None:
        return []

    levels = []
    level = 0
    queue = []
    queue.append(root)

    while len(queue) > 0:
        for _ in range(len(queue)):
            curr = queue.pop(0)

            if len(levels) <= level:
                levels.append([])

            levels[level].append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        level += 1

    return levels
