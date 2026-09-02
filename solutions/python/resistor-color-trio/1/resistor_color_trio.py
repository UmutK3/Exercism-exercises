def label(colors):
    color_codes = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }
    first_digit = color_codes.get(colors[0].lower())
    second_digit = color_codes.get(colors[1].lower())
    multiplier = color_codes.get(colors[2].lower())

    resistance_value = (first_digit * 10 + second_digit) * (10 ** multiplier)
    resistance_value = str(resistance_value)
    if resistance_value.endswith("000000000"):
        resistance_value = resistance_value[:-9] + " gigaohms"
    elif resistance_value.endswith("000000"):
        resistance_value = resistance_value[:-6] + " megaohms"
    elif resistance_value.endswith("000"):
        resistance_value = resistance_value[:-3] + " kiloohms"
    else:
        resistance_value += " ohms"
    return resistance_value
print(label(['red', 'violet', 'yellow']))  # Example usage