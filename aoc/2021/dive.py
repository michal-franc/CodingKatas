from simple_unittest  import test

def dive(commands):
    f = 0
    ud = 0
    for c in commands:
        if c[0][0] == 'f':
            f += int(c[1])
        elif c[0][0] == 'd':
            ud += int(c[1])
        elif c[0][0] == 'u':
            ud -= int(c[1])
            if ud < 0:
                ud = 0

    return f * ud




test('basic', dive([
    ['forward', 5],
    ['down', 5],
    ['forward', 8],
    ['up', 3],
    ['down', 8],
    ['forward', 2]
    ]), 150)

inputs = []
file = open('dive_input', 'r')
lines = file.readlines()
for line in lines:
    split = line.strip().split()
    inputs.append(split)
print(dive(inputs))

