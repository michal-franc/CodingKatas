def groupAnagrams_trie(strs):
    return []

# time complexity: O(n*n logn)
# sort is O(nlogn)
def groupAnagrams_sort_compare(strs):
    if len(strs) <= 0:
        return []

    result = {}

    # first basic solution calculate hash and add to set([])
    # basic hash - value of characters
    
    # O(n)
    for word in strs:
        # O(nlogn)
        sorted_word = ''.join(sorted(word))
        if sorted_word not in result:
            result[sorted_word] = [word]
        else:
            result[sorted_word].append(word)

    final_result = []

    for key in result:
        final_result.append(result[key])

    return final_result

# you can get rid of hash collisions by mapping characted to primes
# but this would be O(n*m) complexity where m is sum of all the chars
# this is a bit faster than the sort method
def groupAnagrams_hash(strs):

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    start = ord('a')
    end = ord('z') + 1

    primes_char = {}

    for c in range(start, end):
        primes_char[chr(c)] = primes.pop(0)

    if len(strs) <= 0:
        return []

    result = {}

    # first basic solution calculate hash and add to set([])
    # basic hash - value of characters

    for word in strs:
        word_hash = 1
        for c in word:
            word_hash *= primes_char[c]
        if word_hash not in result:
            result[word_hash] = [word]
        else:
            result[word_hash].append(word)

    final_result = []

    for key in result:
        final_result.append(result[key])

    return final_result

def groupAnagrams(strs):
    return groupAnagrams_hash(strs)

test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(test_input)
