def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    total = 0
    for i in range(1,int(number / 2 + 1)):
        if number % i == 0:
            total += i
    if number == total:
        return "perfect"
    elif number < total:
        return "abundant"
    else:
        return "deficient"

