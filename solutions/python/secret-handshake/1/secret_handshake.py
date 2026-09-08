def commands(binary_str):
    digits = binary_str[-5:][::-1]
    actions = ["wink","double blink","close your eyes","jump"]
    result = []
    for number, x in enumerate(digits):
        if number == 4 and x == "1":
            result.reverse()
            break
        if x == "1":
            result.append(actions[number])
    return result
