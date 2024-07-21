def isValid(paren) -> bool:

    # if only one element nothing to check
    if len(paren) == 1:
        return False

    # if len odd then nothing to check
    # we check odd by using // to get the floor of division and compare it to non floor division
    if len(paren) // 2 != len(paren) / 2:
        return False

    mapOfPars = {}
    mapOfPars[")"] = "("
    mapOfPars["}"] = "{"
    mapOfPars["]"] = "["
 
    # if you see ( { [ enque stack
    # if you see ) } ] dequeue stack only if top is corresponding

    stack = []

    # O(N)
    for x in paren:
        if x == "(" or x == "{" or x == "[":
            stack.append(x)
        else:
            # covers "){" scenario when we started with not opening bracket
            if len(stack) == 0:
                return False

            if stack[-1] == mapOfPars[x]:
                stack.pop()
                continue
            else:
                return False

    # covers scenario that w never had any opening parenthes
    return len(stack) == 0
