from binarytree import TreeNode

def construct_in_post(inorder, postorder):

    # create mapping of value to index so we don't need to search all the time for all the values
    # this will only work for unique values
    vix= {} 
    i = 0
    for x in inorder:
        if x not in vix:
            vix[x] = i

        i = i + 1

    def helper(left_index, right_index):
        
        # this is a way to verify if we still have elements to find
        if left_index > right_index:
            return None

        # we start with observation that last element in post  order is always the root
        rootVal = postorder.pop();
        root = TreeNode(rootVal)
        
        index = vix[rootVal]

        # then we use in order to split the left to right side of the root
        root.right = helper(index+1, right_index)
        root.left = helper(left_index, index-1)
        return root

    return helper(0, len(inorder) -1)

def construct_in_pre(preorder, inorder):

    # create mapping of value to index so we don't need to search all the time for all the values
    # this will only work for unique values
    vix= {} 
    i = 0
    for x in inorder:
        if x not in vix:
            vix[x] = i

        i = i + 1

    def helper(left_index, right_index):

        if left_index > right_index:
            return None
        
        # we start with observation that first element in post  order is always the root
        rootVal = preorder.pop(0)
        index = vix[rootVal]
        root = TreeNode(rootVal)

        # then we use in order to split the left to right side of the root
        root.left = helper(left_index, index-1)
        root.right = helper(index+1, right_index)
        return root

    return helper(0, len(inorder) - 1)
