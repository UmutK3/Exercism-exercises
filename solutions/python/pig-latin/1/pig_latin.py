def translate(text):
    text1 = ("")
    text = text.split()
    for i in text:
        
        possibilities1 = ("a","e","i","o","u","xr","yt")
        startswith = i.startswith(possibilities1)
        if startswith:
            
            text1 = i + "ay" + " "
            continue
        possibilities2 = "bcdfghjklmnpqrstvwxyz"
        consonants = ("")
        a = 1
        for b in i:
            if b in possibilities2:           
                if b == "q" and i[a] == "u":
                    break     
                consonants += b
                if i[a] == "y":
                    break
                a += 1
            else:
                break
        text2 = i[a-1:]
        if text2.startswith("qu"):
            text3 = text2[2:]
            text1 += text3 + consonants + "qu" + "ay" + " "
            continue
        text2 = i[a:]
        if text2.startswith("y"):
            text1 += text2 + consonants + "ay" + " "     
        else:
            text2 = i[a-1:]
            text1 += text2 + consonants + "ay" + " "
    text1 = text1.strip()
    return text1   
print(translate("rhythm"))
        
    

    
        

    
    
