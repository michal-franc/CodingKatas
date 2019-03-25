from simple_unittest import test

def length_of_longest_substring(s):
    
    if len(s) <= 0:
        return 0

    if len(s) == 1:
        return 1

    found = set()
    max_length = 0

    for c in s:
        if c not in found:
            found.add(c)
        else:
            if len(found) > max_length:
               max_length = len(found)
            found.remove(c)

    if len(found) > max_length:
       max_length = len(found)

    return max_length

test('', length_of_longest_substring(''), 0)
test('a', length_of_longest_substring('a'), 1)
test('abcabcbb', length_of_longest_substring('abcabcbb'), 3)
test('abcadbcbb', length_of_longest_substring('abcadbcbb'), 4)
test('bbbbb', length_of_longest_substring('bbbbb'), 1)
test('pwwkew', length_of_longest_substring('pwwkew'), 3)
test('abcd', length_of_longest_substring('abcd'), 4)
