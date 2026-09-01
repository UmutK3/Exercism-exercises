def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if digits == [] or set(digits) == {0}:
        return [0]
    decimal_value = 0
    a = 0
    digits = digits[::-1]
    for digit in digits:
        decimal_value += digit * input_base ** a
        a += 1
    output = []
    while decimal_value > 0:
        output.append(decimal_value % output_base)
        decimal_value //= output_base
    return output[::-1]

        
    