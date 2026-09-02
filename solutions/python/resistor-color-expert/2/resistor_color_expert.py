def resistor_label(colors):
    color_values = {"black": [0,""],
                    "brown": [1,1],
                    "red": [2,2],
                    "orange": [3,""],
                    "yellow": [4,""],
                    "green": [5,0.5],
                    "blue": [6,0.25],
                    "violet": [7,0.1],
                    "grey": [8, 0.05],
                    "white": [9,""],
                    "gold" : ["",5] ,
                    "silver": ["",10]
                    }
    if len(colors) == 1:
        return "0 ohms"
    color1_value = color_values.get(colors[0])[0]
    color2_value = color_values.get(colors[1])[0]
    multiplier = 10 ** color_values.get(colors[-2])[0]
    total_value = (color1_value * 10 + color2_value) * multiplier
    if len(colors) == 5:
        color3_value = color_values.get(colors[2])[0]
        total_value = (color1_value * 100 + color2_value * 10 + color3_value) * multiplier
    else:
        color3_value = None
    if total_value >= 1000000:
        unit = "megaohms"
        total_value /= 1000000
    elif total_value >= 1000:
        unit = "kiloohms"
        total_value /= 1000
    else:
        unit = "ohms"
    tolerance = color_values.get(colors[-1])[1]
    if color3_value:
        return f"{int(total_value) if total_value.is_integer() else total_value} {unit} ±{tolerance}%"
    return f"{int(total_value) if total_value.is_integer() else total_value} {unit} ±{tolerance}%"
print(resistor_label(["red", "green", "yellow", "yellow", "brown"]))                   