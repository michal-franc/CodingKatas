# 1. the most obvious brute force solution if looping for each s through T but this will lead to O(n^2) time complexity

# 2. first count all the characters into hashmap with key to be char and coutner as value
# this will lead to hashmap like a -> 2 b -> 1
# then for next string go through it - lookup if char exists and has counter > 0 if not its not anagram
# then remove from hasmap decreasing counter and if you hit 0 remove the key
# at the end check if hashmap is empty done
# thanks to this you will get average O(n) as we will loop O(n) 2 times
# time coplexity O(n)
# space complexity O(n)

def isAnagram(s, t):
    # O(N) space
    counter = {}

    # O(N) time
    for c in s:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1

    for c in t:
        if c not in counter:
            return False
        else:
            if counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1

    return len(counter) == 0
