def lengthOfLongestSubstring(s):
    
    if len(s) <= 1:
        return len(s)

    n = len(s)
    map = {}
    i = 0
    j = 0
    maxCount = 0

    while i < n and j < n:
        cj = s[j]
        if cj not in map:
            map[cj] = 1
            j += 1
            maxCount = max(maxCount, j - i)
        else:
            ci = s[i]
            del map[ci]
            i += 1

    return maxCount
