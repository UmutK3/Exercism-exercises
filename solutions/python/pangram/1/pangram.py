import string

def is_pangram(sentence):
    a = ' ._"-?!:,;'
    sentence = sentence.lower()
    alphabet = string.ascii_lowercase
    letters_found = ""
    for i in sentence:
        if i in a or i in letters_found:
            continue
        if i in alphabet:
            letters_found += i
    for x in alphabet:
        if x in letters_found:
            continue
        else:
            return False
    return True


        
