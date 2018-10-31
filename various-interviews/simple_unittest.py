from termcolor import colored

def test(text, value, expected):
    if value == expected:
        print colored("V: for %s - expected '%s' got '%s'" %(text, expected, value), 'green')
    else:
        print colored("X: for %s - expected '%s' got '%s'" %(text, expected, value), 'red')
