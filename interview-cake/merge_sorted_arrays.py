import sys

def merge_arrays(sorted_array_one, sorted_array_two):

    merged_array = []

    one_index = 0
    two_index = 0

    while one_index < len(sorted_array_one) or two_index < len(sorted_array_two):

        if one_index < len(sorted_array_one):
            one_value = sorted_array_one[one_index]
        else:
            one_value = sys.maxint

        if two_index < len(sorted_array_two):
            two_value = sorted_array_two[two_index]
        else:
            two_value = sys.maxint

        if one_value < two_value:
            merged_array.append(one_value)
            one_index += 1
        elif two_value < one_value:
            merged_array.append(two_value)
            two_index += 1

    return merged_array

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [0, 1, 2, 23, 45, 999, 1200, 2000, 99999]

print(merge_arrays(my_list, alices_list))
