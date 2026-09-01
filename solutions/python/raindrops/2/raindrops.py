def convert(number):
    output = ("")
    prime = False
    if number % 3 == 0:
        output += "Pling"
        prime = True
    if number % 5 == 0:
        output += "Plang"
        prime = True
    if number % 7 == 0:
        output += "Plong"
        prime = True
    if prime == False:
        output = str(number)
    return output

        
