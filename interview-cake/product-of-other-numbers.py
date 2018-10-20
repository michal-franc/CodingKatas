def product_of_other_numbers(list_of_ints):

    product_values = [0] * len(list_of_ints)

    # calculate product for before i
    product_so_far = 1
    for i, integer in enumerate(list_of_ints):
        product_values[i] = product_so_far
        product_so_far *= integer

    product_so_far = 1
    # calculate product for after i
    for i in xrange(len(list_of_ints) - 1, -1, -1):
        product_values[i] *= product_so_far
        product_so_far *=  list_of_ints[i]


    return product_values

test_data = [1, 7, 3, 4]

print(product_of_other_numbers(test_data))
