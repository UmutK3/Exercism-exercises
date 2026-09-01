import string
def is_valid(isbn):
    isbn = isbn.translate(str.maketrans("","",string.punctuation))
    numbers = ["X","1","2","3","4","5","6","7","8","9"]
    if len(isbn) < 10 or len(isbn) > 10 or isbn[9] not in numbers:
        return False
    total = 0
    a = 10
    for i in isbn:
        if isbn[9] == i:
            if i == "X":
                i = "10"
        if not i.isdigit():
            return False
        i = int(i) 
        total += i * a
        a -= 1
    return total % 11 == 0
print(is_valid("3-598-P1581-X"))

        
       

