def is_paired(input_string):
    parantheses = {"(":")","[" : "]","{":"}"}
    used_parentheses = []
    for character in input_string:
        if character in parantheses.keys():
           used_parentheses.append(character)
        elif character in parantheses.values():
            if not used_parentheses or character != parantheses[used_parentheses[-1]]:
                return False
            used_parentheses.pop()
    return len(used_parentheses) == 0      