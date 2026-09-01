import string

def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words = list):
    a = 0
    for i in vocab_words[1:]:
        a += 1
        vocab_words[a] = vocab_words[0] + i
    return " :: ".join(vocab_words)

def remove_suffix_ness(word):
    for i in range(len(word)):
        if word[i:] == "ness":
            if word[i-1] == "i":
                return word[:i-1] + "y"
            return word[:i]
        
def adjective_to_verb(sentence, index):
    list1 = [i.strip(string.punctuation) for i in sentence.split()]
    return list1[index] + "en"
print(adjective_to_verb('I need to make that bright.', -1 ))
    
    