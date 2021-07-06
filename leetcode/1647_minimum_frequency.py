from simple_unittest import test
import math

# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.


# idea is simple
# we sort the array to simplify traversal to build count array for the cost of O(nlogn)
# we then go through string and build an array of counts of chars
# [1, 0, 2, 3, 1, 1]
# Then we need to make this array to only contain 1s and 0s


def minDelFrequency(value): #800ms - mem 20MB
    # with sort we have O(nlogn) + O(n^2) - worst case
    # with sort we have O(nlogn) + O(n) - best case

    # sort O(nlogn)
    sortedValue = sorted(value)

    # set size of intermediary array
    # index -> count number
    # value -> number of chars with this cound

    # this is not optimal and most likley can be improved a lot
    # its completetly not optimal if we have `aaaaaaaaaaaaaa` as then we only need `1` space but we create it a lot bigger
    counterArr = [0]*len(value)

    current = sortedValue[0]
    counter = -1

    # O(n) - creating array of index = count, value = chars with this count
    for c in sortedValue:
        if c != current:
            counterArr[counter]+=1
            counter = -1
            current = c
        counter+=1

    # handle last char in array as it wont hit any char change to trigger update of this array
    counterArr[counter]+=1

    # this is our result at the end
    numberOfDeletions = 0

    # stack to contain empty spaces
    # we ust stack here to maintain easilly list of `last closest empty spaces`
    lastAvailableFreeSpace = []

    for i in range(len(counterArr)-1):
        index = i+1
        val = counterArr[i]

        if counterArr[i] == 1:
            # if its already - 1 we dont need to do anything
            continue

        if counterArr[i] == 0:
            # if its - 0 then this is a free space we add its index to stack
            lastAvailableFreeSpace.append(i)
            continue

        # if its not 0 or 1 then we need to find space to move this char number
        # we need to find how many to find space
        # -1 as one unique char can stay on this count
        howManyToFind = (val - 1)
        # we need to iterate through number of how many to find an try to find space
        # go through all the chars and try to find them space
        for _ in range(howManyToFind):
            # if there is no available free space then we have to remove this char as subsequent lower spaces are not available
            # then given index X - which means count of chars 
            # and value - which mean number of uniqe chars with this count
            # then index * occurence - 1 == number of deletions
            if len(lastAvailableFreeSpace) == 0:
                numberOfDeletions += index * howManyToFind
                break
            else:
                lastIndexWithSpace = lastAvailableFreeSpace.pop()
                distanceToLastSpace = (i + 1) - (lastIndexWithSpace + 1)
                numberOfDeletions += distanceToLastSpace
                # we found space so we can lower the number of how many we need to find still
                howManyToFind -= 1
        
    return  numberOfDeletions

def minDelFrequency2(value):
    minDel=0 

    # count frequency
    # index - char
    # value - frequency
    d={}
    for i in set(value):
        d[i]=value.count(i) 


    
    helper=set()
    # iterate from lowest frequency to the highest
    for freq in sorted(d.values(),reverse=True):
        # try to insert frequency to set and look for space
        while freq in helper:
            freq -=1 
            minDel +=1 
        # if the freq is 0 then we had to remove all the chars
        # if not then this is unique frequency
        if freq:
            helper.add(freq)
    return minDel

test('aab', minDelFrequency2("aab"), 0)
test('abcabc', minDelFrequency2("abcabc"), 3)
test('aaabbbcc', minDelFrequency2("aaabbbcc"), 2)
test('aaabbbccc', minDelFrequency2("aaabbbccc"), 3)
test('ceabaacb', minDelFrequency2("ceabaacb"), 2)
test('abbcccddddeeeeffff', minDelFrequency2("abbcccddddeeeeffff"), 8)
test('big', minDelFrequency2("abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz"), 276)