def compress(s:str) -> str :
    comp = ""

    currentChar = s[0]
    currentCount = 0
    index = 0

    for c in s:
        if c != currentChar or currentCount == 9:
            comp += str(currentCount) + currentChar
            currentChar = c
            currentCount = 0
        currentCount += 1
        index += 1
    
    # handle last char
    comp += str(currentCount) + currentChar

    return comp
