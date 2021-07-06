from simple_unittest  import test

def maskify(number):

    if len(number) <= 4:
        return number

    return ''.join((["#"] * (len(number)-4))) + number[len(number)-4:]

test('', maskify(''), '')
test('1', maskify('1'), '1')
test('123456789', maskify('123456789'), '#####6789')