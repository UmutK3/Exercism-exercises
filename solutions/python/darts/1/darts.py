def score(x, y):
    if x ** 2 + y ** 2 > 10 ** 2:
        return 0
    elif x ** 2 + y ** 2 <= 10 ** 2:
        if x ** 2 + y ** 2 > 5 ** 2:
            return 1
        elif x ** 2 + y ** 2 <= 5 ** 2:
            if x ** 2 + y ** 2 > 1 ** 1:
                return 5
            else:
                return 10

        
