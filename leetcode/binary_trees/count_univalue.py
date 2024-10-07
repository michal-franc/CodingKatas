def countUnivalue(root):
    if root == None:
        return 0

    # to ignore root
    counter = 0

    def recIn(node):
        nonlocal counter
        if node == None:
            return True

        isLeft = recIn(node.left)
        isRight = recIn(node.right)

        if isLeft and isRight:
            if node.left and node.left.val != node.val:
                return False

            if node.right and node.right.val != node.val:
                return False

            counter += 1
            return True

        return False

    recIn(root)

    return counter
