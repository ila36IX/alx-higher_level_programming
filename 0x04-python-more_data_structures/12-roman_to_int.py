#!/usr/bin/python3


def roman_to_int(roman_string):
    if (type(roman_string) != str and roman_string == None):
        return (0)
    equiled_digit = 0
    units = {
        'VIII': 8,
        'VII': 7,
        'III': 3,
        'IX': 9,
        'VI': 6,
        'IV': 4,
        'II': 2,
        'V': 5,
        'I': 1
    }
    tens = {
        'LXXX': 80,
        'LXX': 70,
        'XXX': 30,
        'XC': 90,
        'LX': 60,
        'XL': 40,
        'XX': 20,
        'L': 50,
        'X': 10
    }
    Hundreds = {
        'DCCC': 800,
        'CCC': 300,
        'DCC': 700,
        'CM': 900,
        'DC': 600,
        'CD': 400,
        'CC': 200,
        'D': 500,
        'C': 100
    }
    Thousands = {
        'MMM': 3000,
        'MM': 2000,
        'M': 1000
    }

    for rom, dig in units.items():
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    for rom, dig in tens.items():
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    for rom, dig in Hundreds.items():
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    for rom, dig in Thousands.items():
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    return (equiled_digit)
