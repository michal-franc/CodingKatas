from simple_unittest  import test

def rec_count_level(arr, stack):
    if not isinstance(arr, list):
        stack.append(0)
        return

    if len(arr) == 0:
        stack.append(-1)
    else:
        stack.append(len(arr))

    for x in arr:
        if isinstance(x, list):
            rec_count_level(x, stack)
        else:
            stack.append(0)


# this solution traverses whole structure twice
# its not optimal it would be better to terminate early when we hit discrepency
def same_structure_as_total(one, two):
    # if one not array then other has to bea rray otwherwise false
    if not isinstance(one, list):
        return not isinstance(two, list)

    if not isinstance(two, list):
        return not isinstance(one, list)

    stackOne = []
    rec_count_level(one, stackOne)
    stackTwo = []
    rec_count_level(two, stackTwo)

    if len(stackOne) != len(stackTwo):
        return False

    while len(stackTwo) > 0:
        if stackOne.pop() != stackTwo.pop():
            return False
    return True

def rec_optimal(one, two):
    for i, _ in enumerate(one):
        if isinstance(one[i],list) and isinstance(two[i], list):
            if len(one[i]) != len(two[i]):
                return False

            if not rec_optimal(one[i], two[i]):
                return False

        elif not isinstance(one[i],list) and not isinstance(two[i], list):
            continue
        else:
            return False

    return True


# this solution tries to quit early when difference is found
def same_structure_as(one, two):
    # if one not array then other has to bea rray otwherwise false
    if not isinstance(one, list):
        return not isinstance(two, list)

    if not isinstance(two, list):
        return not isinstance(one, list)

    if len(one) != len(two):
        return False

    return rec_optimal(one, two)

test(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
test(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
test(same_structure_as([[[],[]]], [[1,1]]), False, "what")
