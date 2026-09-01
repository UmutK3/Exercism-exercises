def color_code(color):
    code = 0
    for color1 in colors():
        if color1 == color:
            return code
        code += 1
        
def colors():
    return ["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]
