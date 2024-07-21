from simple_unittest import test

def combination_sum(candidates, target):

    if target <= 0:
        return []

    sorted_candidates = sorted(candidates, reverse=True)
    result = []

    for x in sorted_candidates:
        if x == target:
            result.append([x])

        if x < target:
            leftovers = combination_sum(candidates, target - x)
            if len(leftovers):
                for i in leftovers:
                    result.append(i + [x])
        else:
            continue

    return []


test('[2, 3, 6, 7]', combination_sum([2, 3, 6, 7], 7), [[7], [2,2,3]])
test('[2, 3, 5]', combination_sum([2, 3, 5], 8), [[2,2,2,2], [2,3,3], [3,5]])
