import string

def rotate2(text2, key):   
    key = int(key)
    number = 0
    text1 = ""
    alphabet = string.ascii_lowercase
    alphabet2 = alphabet.upper()
    
    for i in text2:
        if i not in alphabet and i not in alphabet2:
            text1 += i
            continue
        elif i in alphabet:
            number = alphabet.index(i)
        else:
            number = alphabet2.index(i)
            
        number += key
        
        if number >= 26:
            number = number - 26
        if i in alphabet2:
            text1 += alphabet2[number]
        else:
            text1 += alphabet[number]
            
    return text1

def rotate(text, key):
    return " ".join(rotate2(text2, key) for text2 in text.split())
