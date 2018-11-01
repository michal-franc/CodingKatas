from simple_unittest import test

# in plce using 'bigger' number
def add_binary(one, two):

    if len(one) >= len(two):
        bigger_array = list(one)
        smaller_array = list(two)
    else:
        bigger_array = list(two)
        smaller_array = list(one)

    bigger_index = len(bigger_array) - 1
    smaller_index = len(smaller_array) - 1

    carry = 0

    while bigger_index >= 0 and smaller_index >= 0:
        bigger_val = int(bigger_array[bigger_index])
        smaller_val = int(smaller_array[smaller_index])

        plus = bigger_val + smaller_val + carry
        
        if plus > 1:
            carry = 1
            bigger_array[bigger_index] = '0'
        else:
            carry = 0
            bigger_array[bigger_index] = str(plus)

        bigger_index -= 1
        smaller_index -= 1

    # if there is still carry just go through the bigger number
    while carry > 0 and bigger_index >= 0:
        bigger_val = int(bigger_array[bigger_index])
        plus = bigger_val + carry

        if plus > 1:
            carry = 1
            bigger_array[bigger_index] = '0'
        else:
            carry = 0
            bigger_array[bigger_index] = str(plus)

        bigger_index -= 1
        
    return ''.join(bigger_array)

test('0001 + 0000 = 0001', add_binary('0001', '0000'), '0001')
test('0000 + 0000 = 0000', add_binary('0000', '0000'), '0000')
test('00000001 + 0000 = 0001', add_binary('000000001', '0000'), '000000001')
test('0000 + 00000001 = 0001', add_binary('0000', '000000001'), '000000001')
test('1000 + 00001001 = 00010001', add_binary('1000', '00001001'), '00010001')
