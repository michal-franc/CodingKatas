# Discussion:

def min_to_0(array):

    a = array[0]
    b = array[1]
    c = array[2]

    if a < b and a < c:
        array[0] = a
        array[1] = b
        array[2] = c

    if b < a and b < c:
        array[0] = b
        array[1] = a
        array[2] = c

    if c < a and c < b:
        array[0] = c
        array[1] = b
        array[2] = a

    return array

def highest_product_of_three(list_of_ints):

    a_b_c = min_to_0([list_of_ints[0], list_of_ints[1], list_of_ints[2]])
    for next_int in list_of_ints[3:]:
        if next_int > a_b_c[0]:
            a_b_c[0] = next_int

        a_b_c = min_to_0(a_b_c)

    return sum(a_b_c)

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 10, 1, 2, 3, 80]
# result = 23

print(highest_product_of_three(test_list))
