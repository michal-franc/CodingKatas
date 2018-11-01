from simple_unittest import test

roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

substraction_pairs = set(['IV', 'IX', 'XL', 'XC', 'CD', 'CM'])

def roman_to_int(roman_string):
    result = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i] + roman_string[i + 1] in substraction_pairs:
            result += (roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]])
            i += 2
        else:
            result += roman_dict[roman_string[i]]
            i += 1

    return result

test('III', roman_to_int('III'), 3)
test('XII', roman_to_int('XII'), 12)
test('XXII', roman_to_int('XXII'), 22)
test('XXVII', roman_to_int('XXVII'), 27)
test('IV', roman_to_int('IV'), 4)
test('LVIII', roman_to_int('LVIII'), 58)
test('MCMXCIV', roman_to_int('MCMXCIV'), 1994)



