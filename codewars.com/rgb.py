from simple_unittest import test

def mapHex(number):
    if number >= 10:
        if number == 10:
            return "A"
        if number == 11:
            return "B"
        if number == 12:
            return "C"
        if number == 13:
            return "D"
        if number == 14:
            return "E"
        if number == 15:
            return "F"
    else:
        return str(number)

def toHex(number):

    if number < 0:
        return "00"

    if number > 255:
        return "FF"

    one = number // 16 
    two = number % 16

    return mapHex(one) + mapHex(two)

def rgb(r, g, b):
    return toHex(r) + toHex(g) + toHex(b)

test(rgb(0,0,0),"000000", "testing zero values")
test(rgb(1,2,3),"010203", "testing near zero values")
test(rgb(255,255,255), "FFFFFF", "testing max values")
test(rgb(254,253,252), "FEFDFC", "testing near max values")
test(rgb(-20,275,125), "00FF7D", "testing out of range values")