import string

def is_pangram(sentence):
    unwanteds = ' ._"-?!:,;'
    sentence = sentence.lower()
    alphabet = string.ascii_lowercase
    letters_found = ""
    for letter in sentence:
        if letter in unwanteds or letter in letters_found:
            continue
        if letter in alphabet:
            letters_found += letter
    for letter2 in alphabet:
        if letter2 in letters_found:
            continue
        return False
    return True


        
