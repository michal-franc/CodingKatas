from simple_unittest  import test

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(sentence):

    letters_count = 26
    s = set()
    # put char to set to make it unique then sum all the chars and check count of set
    for c in sentence.lower():
        if c.isalpha():
            s.add(c)
    return  len(s) == letters_count

test('The quick, brown fox jumps over the lazy dog!', is_pangram('The quick, brown fox jumps over the lazy dog!'), True)