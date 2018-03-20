import unittest

def reverse_integer_iterative(i):

    if i is None:
        return -1

    numbers = list(str((i)))

    if i >= 0:
        start = 0
    else:
        start = 1

    end = len(numbers) - 1

    while start < end:
        buff = numbers[start]
        numbers[start] = numbers[end]
        numbers[end] = buff

        start += 1
        end -= 1

    res = int(''.join(numbers))

    if abs(res) > (2 ** 31 - 1):
        return 0
    else:
        return res

def reverse_integer_2(i):

    if i is None:
        return -1

    if i >= 0:
        sign = ''
        start = None
    else:
        sign = '-'
        start = 0

    res = int(sign + ''.join(str(i)[:start:-1]))

    if abs(res) > (2 ** 31 - 1):
        return 0
    else:
        return res

def reverse_integer(i):

    if i is None:
        return -1

    if i >= 0:
        multiplier = 1
    else:
        multiplier = -1

    res = int(str(abs(i))[::-1])

    if abs(res) > (2 ** 31 - 1):
        return 0
    else:
        return multiplier * res


class ReeerseIntegerTests(unittest.TestCase):

    def test_none(self):
        data = None
        actual = reverse_integer(data)

        self.assertEquals(-1, actual)

    def test_fake_overflow(self):
        data = None
        actual = reverse_integer(data)

        self.assertEquals(-1, actual)

    def test_2_reverse(self):
        data = 12
        actual = reverse_integer(data)

        self.assertEquals(21, actual)

    def test_negative(self):
        data = -12
        actual = reverse_integer(data)

        self.assertEquals(-21, actual)

    def test_3_reverse(self):
        data = 321
        actual = reverse_integer(data)

        self.assertEquals(123, actual)

    def test_10_reverse(self):
        data = 3211234521
        actual = reverse_integer(data)

        self.assertEquals(1254321123, actual)

