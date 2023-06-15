#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_num_sp = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    roman_int = 0
    prev_val = 0
    for char in reversed(roman_string):
        for key, value in roman_num_sp.items():
            if char == key:
                if value < prev_val:
                    roman_int = roman_int - value
                else:
                    roman_int = roman_int + value
                    prev_val = value
    return roman_int
