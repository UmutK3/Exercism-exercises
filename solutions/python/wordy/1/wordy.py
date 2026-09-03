def answer(question):
    if not question.startswith("What is") or not question.endswith("?"):
        raise ValueError("syntax error")
    process = question[7:-1].strip()
    process = process.replace("multiplied by", "multiplied")
    process = process.replace("divided by", "divided")
    if not process:
        raise ValueError("syntax error")
    process = process.split()
    try:
        value = int(process[0])
    except ValueError:
        raise ValueError("syntax error")
    a = 1
    b = len(process)
    while a < b:
        type1 = process[a]
        if a + 1 >= b:
            if type1 == "cubed":
                raise ValueError("unknown operation")
            raise ValueError("syntax error")
        try:
            next_value = int(process[a + 1])
        except ValueError:
            raise ValueError("syntax error")
        if type1 == "plus":
            value += next_value
        elif type1 == "minus":
            value -= next_value
        elif type1 == "multiplied":
            value *= next_value
        elif type1 == "divided":
            value //= next_value
        else:
            raise ValueError("unknown operation")
        a += 2 
    return value

     
