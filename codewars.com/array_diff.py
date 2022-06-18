from simple_unittest  import test

def array_diff_n2(a, b):

    # for a
    # for b
    # check if a === b
    # add to buffer
    # but this is O(n2)

    buf = []
    found = False

    for aa in a:
        for bb in b:
            if aa == bb:
                found = True;
                break;
        if not found:
            buf.append(aa);

        found = False;
    return buf;

def array_diff(a, b):
    # O(n) through b list add to dict if number exists
    # go through a list and check if item exists in dict O(1)
    # if not add to buff
    # Then it should be O(n) + O(n)

    dic = {};
    for bb in b:
        if bb not in dic:
            dic[bb] = True;

    buf = []
    for aa in a:
        if aa not in dic:
            buf.append(aa);

    return buf

test('removing element that is only there', array_diff([1, 1, 1, 1],[1]), []);
test('[1,2,3],[1]', array_diff([1, 2, 3],[1]), [2,3]);
test('[1,2,3],[1,3]', array_diff([1, 2, 3],[1,3]), [2]);
test('[1,2,2],[1,2]', array_diff([1, 2, 2],[1,2]), []);
test('[1,2,2],[1,2]', array_diff([1, 2, 2, 4, 11],[1, 11]), [2, 2, 4]);
test('basic empty array', array_diff([],[]), []);
    
