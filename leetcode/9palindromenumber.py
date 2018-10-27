from simple_unittest import test
from math import log, ceil

def is_palindrome_number(number):

    # this is one digit number without a sign its always a palindrome
    if number < 10 and number >= 0:
        return True

    # number with a sign is always false as sign is not represented on the right side
    if number < 0:
        return False

    # we can change the value to str and then do a comparison but ... it is better to use %
    # observe that given 212
    # 212 / 100 = 2
    # 2 / 1 = 2 
    # 2 == 2 => True
    # using division we can get single digints and then 'compare them'
    # we can then have two counters left and right
    # right starts with 1
    # left starts with x000
    # we multiply right by 10 and divide left by 10
    # each step using them to calculate division and check if value matches

    # to calculate how big is left we will use log with base 10 
    # log_10 212 -> 2.xxxx -> so we now its 2 0
    # left = 10^2

    # so getting left digit is easy 
    # 212 -> 200 / 100 -> 2

    # how to get right digit?
    # 212 % (212 / 10) -> 2

    # 99 % (99 / 10) -> 0

    left_divisor = pow(10, int(log(number, 10)))
    right_divisor = 10
    #print "start number: %s" % number

    while number >= 1:
        # we covers case with single digit number
        div = number / right_divisor
        if div < 10:
            div = 10

        right_digit = number % div
        left_digit = number / left_divisor

        #print "     l_divisor: %s" % left_divisor
        #print "     left: %s , right: %s" % (left_digit, right_digit)

        if left_digit != right_digit:
            return False

        # now we need to shrink our number
        # example:
        # 11211
        # after first step we need to have 121 to check
        # 11211 -> 121
        # 11211 - (left_divisor * left_digit)
        # _1211
        # 11211 / right_divisor (10)
        # _121_

        # if next digit is zero? dont change number? but left divisor?

        number -= (left_divisor * left_digit)
        number /= right_divisor

        # we move left divisor by 20^2 as two digits moved
        left_divisor /= 100
        #print "end number: %s" % number

    return True

test("1009009001", is_palindrome_number(1009009001), True)
test("1100011", is_palindrome_number(1100011), True)
test("100", is_palindrome_number(100), False)
test("1000", is_palindrome_number(1000), False)
test("1000000", is_palindrome_number(1000000), False)
test("1000001", is_palindrome_number(1000001), True)
test("0", is_palindrome_number(0), True)
test("121", is_palindrome_number(121), True)
test("10", is_palindrome_number(10), False)
test("11", is_palindrome_number(11), True)
test("-121", is_palindrome_number(-121), False)
test("1", is_palindrome_number(1), True)
test("111999", is_palindrome_number(111999), False)
test("111999111", is_palindrome_number(111999111), True)
test("11199911", is_palindrome_number(11199911), False)
test("1000021", is_palindrome_number(1000021), False)
