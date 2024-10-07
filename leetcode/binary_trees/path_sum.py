def hasPathSum(root, target):
    if root == None:
        return 0

    res = False

    def recIn(root, currSum):
        nonlocal res
        if root == None:
            return

        # we only want to check at the `end` of tree in the leaf node
        if root.left == None and root.right == None:
            if target == currSum + root.val:
                res = True

        recIn(root.left, currSum + root.val)
        recIn(root.right, currSum + root.val)

    recIn(root, 0)

    return res
