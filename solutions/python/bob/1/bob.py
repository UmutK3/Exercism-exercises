def response (hey_bob = None):
    if not hey_bob  or not hey_bob.strip():
        return "Fine. Be that way!"
    hey_bob = hey_bob.strip()
    is_question = hey_bob.endswith("?")
    is_shout = hey_bob.isupper()
    if is_question and is_shout:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_shout:
        return "Whoa, chill out!"
    else:
        return "Whatever."
   
