def egg_count(display_value):
    count = 0
    while display_value >= 1:
        binary = display_value % 2
        display_value //= 2
        count += 1 if binary == 1 else 0
    return count