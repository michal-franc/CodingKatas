from simple_unittest  import test

#def rec_perm(jjj):

def permutations(string):
    if len(string) == 1: 
        return [string];
    if len(string) == 2: 
        return [string[0] + string[1], string[1] + string[0]]

    result = []
    for s in string:
        return permutations(s[1:])

    return result

test('a', permutations('a'), ['a']) 
test('ab', permutations('ab'), ['ab', 'ba']) 
test('abc', permutations('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) 
