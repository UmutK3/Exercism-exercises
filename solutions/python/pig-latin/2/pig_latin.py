def translate_word(word):
    
    if word[0] in "aeiou" or word.startswith(("xr","yt")):
        return word + "ay"
    
    for i in range(len(word)):
        if word[i:i+2] == "qu":
            return word[i+2:] + word[:i+2] + "ay"
        
        if word[i] in "aeiou" or (i > 0 and word[i] == "y"):
            return word[i:] + word[:i] + "ay"
        
def translate(text):
    return " ".join(translate_word(word) for word in text.split())
print(translate("quick fast run"))