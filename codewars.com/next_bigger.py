from simple_unittest  import test

# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

# 1. iterate through digits - n
# 2. go from the end and try to move last element to the first place that its higher 

def next_bigger(number):
    # we convert number to reversed array of integers
    numberStr = [int(x) for x in str(number)][::-1]
    lastNumber = numberStr[0]
    lastNumberIndex = 0

    # we ignore first (last) number
    # as we ignore first element we set indexCounter to 1
    indexCounter = 1
    for i in numberStr[1:]:
        if i < lastNumber:
            numberStr[indexCounter] = lastNumber
            numberStr[lastNumberIndex] = i
            break
        elif i == lastNumber:
            lastNumberIndex = indexCounter
        
        indexCounter+=1

    # we reverse the array and just create strign and then int out of it
    return int(''.join(str(e) for e in numberStr[::-1]))




test('12', next_bigger(12),21)
test('513', next_bigger(513),531)
test('2017', next_bigger(2017),2071)
test('414', next_bigger(414),441)
test('144', next_bigger(144),414)
test('145', next_bigger(145),154)
test('165', next_bigger(165),516)