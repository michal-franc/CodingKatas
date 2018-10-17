


def reverse_string(input_string):

    left_index = 0
    right_index = len(input_string) - 1

    while left_index < right_index:

        test_string[left_index], test_string[right_index] = test_string[right_index], test_string[left_index]

        left_index += 1
        right_index -= 1

    return input_string


test_string = ['a', 'b', 'c', 'd', 'a']
print(reverse_string(test_string))
