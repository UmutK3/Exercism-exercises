import string

def is_isogram(phrase):
    phrase = "".join(phrase.lower().split())
    a = [i for i in phrase if i in string.punctuation]
    letters = ("")
    for letter in phrase:
        if letter in a:
            continue
        if letter in letters:
            return False
        letters += letter
    return True

        
