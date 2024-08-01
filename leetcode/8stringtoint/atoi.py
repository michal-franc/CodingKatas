def atoiv1(s):

    numberStarted = False
    sign = ''

    numbers = []

    # get the numbers
    for c in s:
        if c == ' ':
            if numberStarted == False and sign == '':
                continue;
            else:
                # if we already started checking numbers and we found " " then ignore
                break;

        if c == '-' or c == '+' :
            if numberStarted or sign != '':
                break;
            sign = c
            continue;

        else:
            nr = ord(c) - ord('0')
            if nr >= 0 and nr <= 9:
                numberStarted = True
                numbers.append(nr)
            else:
                break;


    # reverse the list counter and use it as 10 power value
    nrCounter = 0
    number = 0
    for n in reversed(numbers):
        number    += n * pow(10, nrCounter)
        nrCounter += 1

    if sign == '-':
        number = min(pow(2,31), number)
        return -number
    else:
        number = min(pow(2,31) - 1, number)
        return number

# faster thanks to 
# - lack of try catch
# - lack of numbers[] so memory used should be lower
def atoi(s):

    numberStarted = False
    sign = ''

    nrCounter = 0
    number = 0
    # get the numbers
    for c in s:
        if c == ' ':
            if numberStarted == False and sign == '':
                continue;
            else:
                # if we already started checking numbers and we found " " then ignore
                break;

        if c == '-' or c == '+' :
            if numberStarted or sign != '':
                break;
            sign = c
            continue;

        else:
            nr = ord(c) - ord('0')
            if nr >= 0 and nr <= 9:
                numberStarted = True
                number    = number * 10 + nr
                nrCounter += 1
            else:
                break;

    if sign == '-':
        number = min(pow(2,31), number)
        return -number
    else:
        number = min(pow(2,31) - 1, number)
        return number
