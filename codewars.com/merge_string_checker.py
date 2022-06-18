from simple_unittest  import test

def is_merge(s, part1, part2):

    iterator_1 = 0
    iterator_2 = 0

    for c in s:
        if iterator_1 < len(part1) and part1[iterator_1] == c:
            iterator_1 +=1
            continue;

        if iterator_2 < len(part2) and part2[iterator_2] == c:
            iterator_2 +=1
            continue;

        return False

    if iterator_1 + iterator_2 < len(part1) + len(part2):
        # not all the values in parts were used its invalid
        return False

    return True

test('basic codewars test', is_merge("codewars", "cdw", "oears"), True);
test('invalid case', is_merge("codewars", "cwd", "oears"), False);
test('one array case', is_merge("cod", "cod", ""), True);
test('one array case 2', is_merge("cod", "", "cod"), True);
test('all empty', is_merge("", "", ""), True);
test('additional characters', is_merge("codewars", "code", "warss"), False);
test('', is_merge("codewars", "codes", "wars"), False);
test('', is_merge("codewars", "co", "w"), False);
