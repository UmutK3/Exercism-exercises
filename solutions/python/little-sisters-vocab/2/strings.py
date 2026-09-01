import string

def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words = list):
    number = 0
    for word in vocab_words[1:]:
        number += 1
        vocab_words[number] = vocab_words[0] + word
    return " :: ".join(vocab_words)

def remove_suffix_ness(word):
    for number in range(len(word)):
        if word[number:] == "ness":
            if word[number-1] == "i":
                return word[:number-1] + "y"
            return word[:number]
        
def adjective_to_verb(sentence, index):
    list1 = [word.strip(string.punctuation) for word in sentence.split()]
    return list1[index] + "en"

    
    