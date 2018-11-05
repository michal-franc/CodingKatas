from simple_unittest import test

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input: ["flower","flow","flight"]
# Output: "fl"

# solution one:
# 1. take first char in first word and check the other if the first char matches
# 2. increment index
# 3. repeat matchin index char until you reach the end of one word (then prefix is this word) or you reach element that doesnt match in one
# space complexity O(1)
# time complexity O(n * m) -> n number of words, m smallest word size

def longestCommonPrefix(strs):

    # there is only one ''
    if len(strs) <= 0:
        return ''

    # whole word is a prefix
    if len(strs) == 1:
        return strs[0]

    index = 0

    # this is O(n)
    smallest_word = min(strs)

    # smallest word is empty  so there is no prefix possible
    if len(smallest_word) <= 0:
        return ''

    not_found_end = True

    while not_found_end and index < len(smallest_word):
        for word_index in range(1, len(strs)):
            if index >= len(strs[word_index]):
                not_found_end = False
                break

            if strs[word_index][index] != strs[0][index]:
                not_found_end = False
                break

        if not_found_end:
            index += 1

    return smallest_word[0:index]

test('basic', longestCommonPrefix(['flower', 'flow', 'flight']), 'fl')
test('fail', longestCommonPrefix(['a', 'ac']), 'a')
test('fail', longestCommonPrefix(['caaa', 'aaaa']), '')
test('fail', longestCommonPrefix(['a']), 'a')
test('fail', longestCommonPrefix(['', 'b']), '')
test('none', longestCommonPrefix(['dog', 'racecar', 'car']), '')
test('long', longestCommonPrefix(['aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaa']), 'aaaaaaaa')
test('empty list', longestCommonPrefix([]), '')

