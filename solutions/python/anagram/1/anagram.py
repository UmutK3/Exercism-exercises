def find_anagrams(word, candidates):
    word = word.lower().replace(" ","")
    result = []
    for candidate in candidates:
        candidate1 = candidate.lower().replace(" ","")
        if word != candidate1 and sorted(word) == sorted(candidate1):
            result.append(candidate)
    return result