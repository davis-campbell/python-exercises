def caesar_cipher(string, shift_factor):
    new_string = ''
    for i in string:
        num = ord(i)
        if num >= 65 and num <= 90:
            num += shift_factor
            if num > 90:
                num -= 26
            elif num < 65:
                num += 26
        elif num >= 97 and num <= 122:
            num += shift_factor
            if num > 122:
                num -= 26
            elif num < 97:
                num += 26
        new_string += chr(num)
    return new_string
