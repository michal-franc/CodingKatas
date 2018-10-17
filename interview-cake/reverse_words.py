
def reverse_string(input_string, left_index, right_index):

    while left_index < right_index:

        test_string[left_index], test_string[right_index] = test_string[right_index], test_string[left_index]

        left_index += 1
        right_index -= 1

    return input_string

def reverse_words(input_string):
    reversed_string = reverse_string(input_string, 0, len(input_string) - 1)

    left = 0

    # +1 on range to cover scenario of (end) otherwise for loop would break and leave last char not changed
    for x in range(len(input_string) + 1):
        if x == len(input_string) or input_string[x] == ' ':
            reverse_string(input_string, left , x - 1)
            left = x + 1

    return reversed_string


test_string = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

print(reverse_words(test_string))
