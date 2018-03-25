import unittest
import random

def get_pivot(array):
    index = int(len(array) / 2)
    return array[index]

def quicksort_with_wastefull_allocation(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = get_pivot(array)
        for val  in array:
            if val < pivot:
                less.append(val)
            elif val == pivot:
                equal.append(val)
            elif  val > pivot:
                greater.append(val)

        less = quicksort(less)
        greater = quicksort(greater)

        return less + equal + greater

    return array

def quicksort_list_comp(array):
    if len(array) <= 1:
        return array
    else:
        pivot = random.choice(array)
        less = [x for x in array if x < pivot]
        equal = [x for x in array if x == pivot]
        greater = [x for x in array if x > pivot]
        return quicksort_list_comp(less) + equal + quicksort_list_comp(greater)

def quicksort(array):
    #__quicksort_in_place(array, 0, len(array) -1)
    #return array

    return quicksort_list_comp(array)

def __quicksort_in_place(array, start, stop):
    if stop - start > 0:
        pivot = array[start]
        left = start
        right = stop

        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1

            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        __quicksort_in_place(array, start, right)
        __quicksort_in_place(array, left, stop)

class QuickSortTests(unittest.TestCase):

    def test_array_with_one_element(self):
        test_data = [1]
        actual = quicksort(test_data)

        self.assertEqual(actual, test_data)

    def test_array_with_two_elements(self):
        test_data = [2, 1]
        actual = quicksort(test_data)

        self.assertEqual(actual, [1, 2])

    def test_array_with_lots_elements(self):
        test_data = [1, 1, 3, 5, 9, 10, 1, 999, 86, 1, 5, 56, 30, 67]
        actual = quicksort(test_data)

        self.assertEqual(actual, [1, 1, 1, 1, 3, 5, 5, 9, 10, 30, 56, 67, 86, 999])

    def test_10_random_lists(self):

        for i in range(10):
            test_data = [int(1000 * random.random()) for i in range(1000)]
            actual = quicksort(test_data)

            self.assertEqual(actual, sorted(test_data))
