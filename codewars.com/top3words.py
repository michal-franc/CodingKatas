# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
from simple_unittest  import test

def incWord(word, wordMap):
    if word not in wordMap.keys():
        wordMap[word] = 0
    wordMap[word] += 1 
    return wordMap

# cpu-O(n)
# mem-O(n) as the dict will grow depending on unique words
# create map of words with counter
def countWords(word):
    nextWordCache = ''
    wordMap = {}
    apostropheCount = 0
    hasLetter = False

    # addiong ' ' space at the end so that we dont need to worry about handling last element
    for n in word.lower()+' ':
        if ord(n) >= ord('a') and ord(n) <= ord('z'):
            nextWordCache += n
            hasLetter = True
            continue
        elif n == '\'':
            # one apostrophe so we can just keep looking for word
            if apostropheCount == 0:
                nextWordCache += n
                apostropheCount += 1
                continue
            else:
                if len(nextWordCache) >= 1 and nextWordCache[0] == '\'' and hasLetter:
                    nextWordCache += n
                    wordMap = incWord(nextWordCache, wordMap)
                    nextWordCache = ''
                    apostropheCount = 0
                    hasLetter = False
        else:
            if hasLetter:
                wordMap = incWord(nextWordCache, wordMap)
                nextWordCache = ''
                apostropheCount = 0
                hasLetter = False

    return wordMap

# partial insert - O(1)
def partialInsert(counts, count, key):
    if counts[0][0] < count:
        return [(count, key), counts[0], counts[1]]

    if counts[1][0] < count:
        return [counts[0], (count, key), counts[1]]

    if counts[2][0] < count:
        return [counts[0], counts[1], (count, key)]

    return counts

# create top3 words
# we could use binary heap for that we could also sort map but this will be more costly O(nlogn) minimum
# using insert in array we make it O(n2)
# but using crazy ugly code :D we can make it O(1)
def getTop3Words(wordMap):
    # as we only expect 3 values we can do this dirty temp array
    # this lets us simplify partial insert
    counts = [(0,''), (0,''), (0,'')]

    # O(n)
    for key in wordMap:
        # O(1)
        counts = partialInsert(counts, wordMap[key], key)

    # reduce the list to only elements that do exist and extract `words`  from tuple
    # O(3)
    result = []
    for x in range(3):
        if counts[x][0] > 0:
            result.append(counts[x][1])

    return result

# O(n)
def top3(word):
    # O(n)
    countedWords = countWords(word) 
    # O(n)
    return getTop3Words(countedWords)

test('1',top3("  //wont won't won't "), ["won't", "wont"])
test('2',top3("  , e   .. "), ["e"])
test('3',top3("  ...  "), [])
test('4',top3("  '  "), [])
test('5',top3("  '''  "), [])

test('a b c', top3('a b c'),['a', 'b', 'c']);
test('a a b b c c d', top3('a a b b c c d'),['a', 'b', 'c']);
test('a b b b c c d d d d e e e e e', top3('a b b b c c d d d d e e e e e'),['e', 'd', 'b']);
test('big', top3("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])
test('big1', top3("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
test('that\'s', top3('that\'s'),['that\'s']);
test('', top3(''),[]);
    
