from simple_unittest import test

# 1. sorted anagrams are the same!

def anagrams(strs):
    result = []

    resultSorted = {}
    for s in strs:
        sortedS = "".join(sorted(s))
        if sortedS in resultSorted:
            resultSorted[sortedS].append(s)
        else:
            resultSorted[sortedS] = [s]

    for key in resultSorted:
        result.append(resultSorted[key])

    return result

test('leetcode example', anagrams(
    ["eat","tea","tan","ate","nat","bat"]
    ), [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ])