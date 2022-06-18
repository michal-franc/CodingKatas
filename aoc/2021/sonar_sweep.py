from simple_unittest  import test

def sweep(measurements):

    prev = -1
    count = 0

    for x in measurements:
        if prev == -1:
            prev = x
            continue

        if x > prev:
            count +=1

        prev = x

    return count

def sweepWindows(measurements):
    count = 0
    cursum = 0
    stack = []
    for x in measurements:
        stack.append(x)
        cursum += x
        if len(stack) == 4:
            nr = stack.pop(0)
            if cursum - nr > cursum - x:
                count += 1

    return count


test('basic', sweep([199,200,208,210,200,207,240,269,260,263]), 7)
test('basic', sweepWindows([199,200,208,210,200,207,240,269,260,263]), 5)

inputs = []
file = open('sonar_sweep_input_1', 'r')
lines = file.readlines()
for line in lines:
    inputs.append(int(line.strip()))
print(sweepWindows(inputs))

