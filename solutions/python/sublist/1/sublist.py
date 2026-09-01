SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    a, b = len(list_one), len(list_two)
    if a > b:
        if any(list_one[i:i + b] == list_two for i in range(a - b + 1)):
            return SUPERLIST
    if a < b:
        if any(list_two[i:i + a] == list_one for i in range(b - a + 1)):
            return SUBLIST
    return UNEQUAL
