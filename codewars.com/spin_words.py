from simple_unittest  import test

def reverse(word):
    ls = len(word)
    rev = [''] * ls
    end = ls-1
    for i in range(ls):
            rev[i] = word[end]
            rev[end] = word[i]
            end-=1
    return "".join(rev)

def spin_words(sentence):

    # first split by space and then do reverse per word
    # O(n) cpu and O(n) mem
    split = sentence.split(' ');

    # list of words but reversed
    new = [];
    # O(n^2) ?? but number of words is lower than N
    # worst case words are single letters then it becomes still O(n) + O(1)
    
    for s in split:
        ls = len(s)
        if ls >= 5:
            new.append(reverse(s))
        else:
            new.append(s)


    return " ".join(new);


test('Welcome', spin_words("Welcome"), "emocleW")
test('The Welcome', spin_words("The Welcome"), "The emocleW")
test('Hey fellow warriors', spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
test('This sentence is a sentence', spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
