def compress(chars) -> int:
    # to track if char has changed
    currentChar = " "
    # to track count of current char
    currentCounter = 0
    # to track where we should put data next
    counterIndex = 0 
    index = 0

    for x in chars:
        if x != currentChar:
            if currentCounter > 1:
                s = str(currentCounter)
                for i in s:
                    counterIndex += 1
                    chars[counterIndex] = i 

            if index != 0:
                counterIndex += 1
                chars[counterIndex] = x

            currentChar = x
            currentCounter = 0

        currentCounter +=1
        index += 1

    if currentCounter > 1:
        s = str(currentCounter)
        for i in s:
            counterIndex += 1
            chars[counterIndex] = i 

    return len(chars[:counterIndex+1])
