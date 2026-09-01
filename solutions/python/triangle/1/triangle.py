def equilateral(Sides = []):
    a = Sides[0]  
    b = Sides[1]  
    c = Sides[2] 
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or a + c < b or b + c < a:
        return False
    if a == b and b == c:
        return True
    else:
        return False 
def isosceles(Sides = []):
    a = Sides[0]  
    b = Sides[1]  
    c = Sides[2] 
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or a + c < b or b + c < a:
        return False
    if a == b or a == c or b == c:
        return True
    else:
        return False

def scalene(Sides = []):
    a = Sides[0]  
    b = Sides[1]  
    c = Sides[2]
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or a + c < b or b + c < a:
        return False
    if a == b or a == c or b == c:
        return False
    else:
        return True

