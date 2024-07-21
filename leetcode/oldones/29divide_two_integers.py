# returns counter and reminder
# checking how many times we can fit in the divisor multiplied by 2
# multipling by two also counter using shifts
def count_divisions(dividend, divisor):

    if divisor == 1:
        return (dividend, 0)
    if divisor == 2:
        return (dividend >> 1, 0)
    if divisor == dividend:
        return (1, 0)

    counter = 1
    # base case is one we assume that number already can fit once
    # 1 -> dividend < divisor
    # so we avoid this case
    # and move to the next one by shifting divisor to the left
    # divisor << 1
    while dividend > (divisor << 1):
        divisor <<= 1
        counter <<= 1

    # next dividend is a reminder that doesnt fit so we return - dividend - divisor
    return (counter, dividend - divisor)

def divide_two_ints(dividend, divisor):

    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)

    counter = 0
    while abs_dividend >= abs_divisor:
        (count , abs_dividend) = count_divisions(abs_dividend, abs_divisor)
        counter += count

    if dividend < 0:
        counter = -counter

    if divisor < 0:
        counter = -counter

    if counter >= (1 << 31):
        return (1 << 31) - 1

    return counter

print(divide_two_ints(10, 5))
print(divide_two_ints(6, 3))
print(divide_two_ints(10, 3))
print(divide_two_ints(7, -3))
print(divide_two_ints(1, 1))
print(divide_two_ints(-1, -1))
print(divide_two_ints(-1, 1))
print(divide_two_ints(-1123213233, 1))
print(divide_two_ints(-1123213233, -1))
print(divide_two_ints(-2147483648, -1))
print(divide_two_ints(2147483647, 2))
