def fizz_buzz(N, M):
    result = []

    for x in range(N, M + 1):

        if x <= 0:
            result.append(str(x))
            continue

        single = []

        if x % 3 == 0:
            single.append('Fizz')
        if x % 5 == 0:
            single.append('Buzz')

        if len(single) <= 0:
            result.append(str(x))
        else:
            result.append("".join(single))

    return ",".join(result)

print(fizz_buzz(1,15))
print(fizz_buzz(0,1))
print(fizz_buzz(-10,1))
