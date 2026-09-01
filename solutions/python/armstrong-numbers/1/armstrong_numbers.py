def is_armstrong_number(number):
    number = str(number)
    total = 0
    for i in number:
        total += int(i) ** len(number)
        if total == int(number):
            return True
    if total != int(number):
        return False
        

        
