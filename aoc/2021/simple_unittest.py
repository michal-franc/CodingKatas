from termcolor import colored

def test(text, value, expected):
    if value == expected:
        print(colored("✓: for %s - expected '%s' got '%s'" %(text, expected, value), 'green'))
    else:
        print(colored("𝗑: for %s - expected '%s' got '%s'" %(text, expected, value), 'red'))
