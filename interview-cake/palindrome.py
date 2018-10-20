def filter_odd_keys(dict_chars):
    return [key for key in dict_chars if dict_chars[key] % 2 != 0]

def can_perm_be_palindrome(input_string):

    char_counter = {}

    for char in input_string:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1 

    non_odd_chars = filter_odd_keys(char_counter)

    # check if there is only one element with count 1 for odd cases
    if len(input_string) % 2 != 0:
        if len(non_odd_chars) > 1:
                return False
    else:
        if len(non_odd_chars) > 0:
                return False

    return True

def can_perm_be_palindrome_using_set(input_string):

    char_counter = set()

    for char in input_string:
        if char in char_counter:
            char_counter.remove(char)
        else:
            char_counter.add(char)

    return len(char_counter) <= 1

test_strings = ["civic", "ivicc", "civil", "livci", "", " ", "aba", "aaaaaaaa", "aaaaaaaabc" ]
for t in test_strings:
    print("for %s it is %s" % (t, can_perm_be_palindrome_using_set(t)))
