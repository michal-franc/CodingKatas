def count_divisions(dividend, divisor):
    counter = 1
   
    # divisor << 1 as i am assuming that divisor at least once fits in the divident
    while dividend > divisor << 1:
        counter <<= 1
        divisor <<= 1

    return counter

def divide_two_ints(dividend, divisor):

    main_counter = 0

    while dividend >= divisor:
        count = count_divisions(dividend, divisor)
        dividend -= count * divisor
        main_counter += count

    return main_counter

print(divide_two_ints(10, 5))
print(divide_two_ints(6, 3))
print(divide_two_ints(10, 3))
print(divide_two_ints(12, 3))
#print(divide_two_ints(7, -3))
print(divide_two_ints(1, 1))
#print(divide_two_ints(-1, -1))
#print(divide_two_ints(-1, 1))
#print(divide_two_ints(-1123213233, 1))
#print(divide_two_ints(-1123213233, -1))
#print(divide_two_ints(-2147483648, -1))
print(divide_two_ints(2147483647, 2))

