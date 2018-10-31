from simple_unittest import test


def is_palindrome_iteration(string):

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True

# time - o(n)
# space - o(1)
# simplest solution reverse string and compare
def is_palindrome_reverse(string):
    return string == string[::-1]

def is_palindrome(string):
    return is_palindrome_iteration(string) 

test('abba', is_palindrome('abba'), True)
test('abbx', is_palindrome('abbx'), False)
test('abb', is_palindrome('abb'), False)
test('aba', is_palindrome('aba'), True)
test('', is_palindrome(''), True)
