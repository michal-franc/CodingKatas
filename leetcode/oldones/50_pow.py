from simple_unittest import test

def myPow(x, n):

    if n == 0:
        return 1

    if n == 1:
        return x

    if n == -1:
        return 1.0/x

    if n % 2 != 0:
        val = myPow(x*x, (abs(n)-1)/2)
    else:
        val = myPow(x*x, abs(n/2))

    if n % 2 != 0:
        val *= x

    if n < 0:
        val = 1.0/val

    if x < 0 and n % 2 != 0:
        val = -abs(val)

    return val

test('if n 0 then return 1', myPow(1, 0), 1)
test('if n 1 then return x', myPow(100, 1), 100)
test('2^2', myPow(2, 2), 4)
test('2^3', myPow(2, 3), 8)
test('2^4', myPow(2, 4), 16)
test('3^3', myPow(3, 3), 27)
test('2^-1', myPow(2, -1), 0.5)
test('2^-2', myPow(2, -2), 0.25)
test('2^-3', myPow(2, -3), 0.125)
test('2^-4', myPow(2, -4), 0.0625)
test('-4^2', myPow(-4, 2), 16)
test('2^-5', myPow(2, -5), 0.03125)
test('edge', myPow(-13.62608, 3), -2529.955504)
