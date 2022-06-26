from termcolor import colored

def test(value, expected, text):
    if value == expected:
        print(colored("✓: for %s - expected '%s' got '%s'" %(text, expected, value), 'green'))
    else:
        print(colored("𝗑: for %s - expected '%s' got '%s'" %(text, expected, value), 'red'))
