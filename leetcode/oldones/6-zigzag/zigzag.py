def convert(s, nRows):

    if nRows == 1:
        return s

    rowDict = {}
    i = 1
    step = -1 

    for c in s:
        if i % nRows == 0 or i == 1:
            step = -step

        rowDict[i] = rowDict.get(i, '') + c
        i += step

    return ''.join(rowDict.values())
