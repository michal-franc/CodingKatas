# find pivot in log(n)
# use binary search using pivot as a breaking point

def sorted_array_search(searched_value, input_array):
    # first lets do binary search
    if len(input_array) <= 0:
        return -1

    if len(input_array) == 1:
        return 1

    pivot = len(input_array) / 2

    if input_array[pivot] == searched_value:
        return pivot

    if searched_value >= input_array[pivot]:
        return pivot + sorted_array_search(searched_value, input_array[pivot:])
    else:
        return pivot - sorted_array_search(searched_value, input_array[:pivot - 1])

test_data = [0, 1, 2, 4, 5, 6, 7, 9, 11]
print(sorted_array_search(9, test_data))

# in place binary search by using low and high - indexes
def find_pivot_in_rotated_array(arr, low_index, high_index):
    
    if low_index == high_index:
        return low_index

    # we need to add low_index as it is inplace algorithm and it is neededd to find correct index
    mid_index = low_index + (high_index - low_index) / 2

    if arr[mid_index] < arr[high_index]:
        return find_pivot_in_rotated_array(arr, low_index, mid_index - 1)
    else:
        return find_pivot_in_rotated_array(arr, mid_index + 1, high_index)

test_data = [4, 5, 6, 7, 0, 1, 2]
print(find_pivot_in_rotated_array(test_data, 0, len(test_data) - 1))

def sorted_rotated_array_search(searched_value, input_array):
    if len(input_array) <= 0:
        return -1

    if len(input_array) == 1 and input_array[0] != searched_value:
        return -1

    pivot = find_pivot_in_rotated_array(input_array, 0, len(input_array) - 1)

    if input_array[pivot] == searched_value:
        return pivot

    if input_array[0] <= searched_value:
        return pivot + sorted_array_search(searched_value, input_array[:pivot -1])
    else:
        return pivot - sorted_array_search(searched_value, input_array[pivot:])

test_data = [4, 5, 6, 7, 0, 1, 2]
print(sorted_rotated_array_search(5, test_data))
