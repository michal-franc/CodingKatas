from simple_unittest import test

def validParenthness(string):

    stack = []

    if len(string) <= 0:
        return True

    for c in string:
        if c == "(":
            stack.append("(")

        if c == ")":
            if len(stack) <= 0:
                return False
            stack.pop()

    return len(stack) <= 0


test('Empty', validParenthness(""), True)
test('()', validParenthness("()"), True)
test(')(()))', validParenthness(")(()))"), False)
test('((()))', validParenthness("((()))"), True)
test(')))(((', validParenthness(")))((("), False)
test('(', validParenthness("("), False)
test('(())((()())())', validParenthness("(())((()())())"), True)
