# solutions

# go through each one with memoization
# loop can be detected if number one number is already in dict
# recursive 

# 1st observation - 6,8 is same as 8,6 - we could memoize it?
# 2nd observation - only 1 with 0 is possible to get True

from simple_unittest import test

def isHappy(n):

    cache = {}

    return recHappyNumber(n, cache)

def recHappyNumber(n, cache):

    if n in cache:
        return False

    newNumber = 0

    for x in str(n):
        if x == '0':
            continue;

        newNumber += pow(int(x),2)

    if newNumber == 1:
        return True

    cache[n] = True
    return recHappyNumber(newNumber, cache)

test('19', isHappy(19), True)
