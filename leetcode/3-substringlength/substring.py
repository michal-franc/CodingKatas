def lengthOfLongestSubstring(s):
    
    if len(s) <= 1:
        return len(s)

    map = {}
    maxCount = 0
    currCount = 0

    for c in s:
        if c in map:
            map = {}
            if currCount > maxCount:
                maxCount = currCount
            currCount = 1
        else:
            currCount += 1

        map[c] = 1

    if currCount > maxCount:
        maxCount = currCount

    return maxCount
