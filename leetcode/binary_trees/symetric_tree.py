from binarytree import TreeNode

def isSymetric(root) -> bool:

    levels = []

    # typical level order implementation using recurrence
    def levelOrder(root, level):

        # levels is a outside contxt that is accesible to all the recurrence elements without passing it
        nonlocal levels

        if len(levels) <= level:
            levels.append([])

        # in normal traversal we can ignore None values
        # but in symmetry task we need None to correctly check tree
        if root == None:
            # this will amplify space complexity by O(x) so not a big deal :D
            levels[level].append(None)
            return
        else:
            levels[level].append(root.val)

        # recurrence happens here its important to jump by 1 level
        levelOrder(root.left, level + 1)
        levelOrder(root.right, level + 1)

    # start level order
    levelOrder(root, 0)

    # pop root as we only need to check symmetry after root
    levels.pop(0)

    for i in range(len(levels)):

        # each level will have multiple pair of items so we need to iterate through level untill its empty
        while levels[i]:
            lvl = levels[i]
            
            # with level order we will have levels that look like this
            # [4, 3, 3, 4]
            # so then it is a matter of comparing  first and last elemenet
            first = lvl.pop(0) 

            if len(lvl) <= 0:
                return False

            last = lvl.pop()

            if first != last:
                return False

    return True
