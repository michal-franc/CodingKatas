from simple_unittest import test

def plus_one(array):

    if len(array) <= 0:
        return []

    carry = True
    current_index = len(array) - 1

    while carry and  current_index >= 0:
        current_number = array[current_index]
        if current_number != 9:
            carry = False
            current_number += 1
        else:
            carry = True

        if not carry:
            array[current_index] = current_number
        else:
            array[current_index] = 0
            current_index -= 1

    if carry:
        return [1] + array

    return array


test('[]', plus_one([]), [])
test('[0]', plus_one([0]), [1])
test('[1, 2, 3]', plus_one([1, 2, 3]), [1, 2, 4])
test('[1, 2, 9]', plus_one([1, 2, 9]), [1, 3, 0])
test('[1, 9, 9]', plus_one([1, 9, 9]), [2, 0, 0])
test('[1, 0, 0]', plus_one([1, 0, 0]), [1, 0, 1])
test('[9, 9, 9]', plus_one([9, 9, 9]), [1, 0, 0, 0])
test('[9]', plus_one([9]), [1, 0])
test('[9, 9]', plus_one([9, 9]), [1, 0, 0])
