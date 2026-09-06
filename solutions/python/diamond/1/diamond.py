import string

letters = string.ascii_uppercase

def rows(letter):
    letter = letter.upper()  # In case a lowercase letter is entered by mistake.
    target_index = letters.index(letter)
    used_letters = letters[:target_index + 1]
    top_half = []

    for index, char in enumerate(used_letters):
        outer_spaces = (target_index - index) * " " 

        if char == "A":
            # If the letter is 'A', there is no inner space.
            top_half.append(outer_spaces + char + outer_spaces) 
            continue
        inner_spaces = (2 * index - 1) * " "
        top_half.append(outer_spaces + char + inner_spaces + char + outer_spaces)
    #  The lower half is the reverse of the upper half.(Except for the letter.)
    bottom_half =  top_half[:-1:][::-1] 
    return top_half + bottom_half

# An example for the code.
print(rows("E")) 