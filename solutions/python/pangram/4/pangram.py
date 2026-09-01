import string

def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = string.ascii_lowercase
    
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
        
