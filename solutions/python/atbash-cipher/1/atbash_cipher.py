import string

def encode(plain_text):
    letters = list(string.ascii_lowercase)
    cipher_text = ""
    for i in plain_text.lower():
        if i in letters:
            cipher_text += letters[-(letters.index(i) + 1)]
        elif i.isdigit():
            cipher_text += i
    return " ".join(cipher_text[i:i+5] for i in range(0,len(cipher_text),5)) 

def decode(ciphered_text):
    return encode(ciphered_text.replace(" ","")).replace(" ","")

