#!/usr/bin/python3


def roman_to_int(roman_string):
    equiled_digit = 0
    units = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9
    }
    tens = {
        'X' : 10,
        'XX': 20,
        'XXX': 30,
        'XL': 40,
        'L': 50,
        'LX': 60,
        'LXX': 70,
        'LXXX': 80,
        'XC': 90
    }
    Hundreds = {
        'C': 100,
        'CC': 200,
        'CCC': 300,
        'CD': 400,
        'D': 500,
        'DC': 600,
        'DCC': 700,
        'DCCC': 800,
        'CM': 900
    }
    Thousands = {
        'M': 1000,
        'MM': 2000,
        'MMM': 3000
    }

    for rom, dig in reversed(sorted(units.items(), key=lambda x: len(x[0]))):
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break;
    for rom, dig in reversed(sorted(tens.items(), key=lambda x: len(x[0]))):
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    for rom, dig in reversed(sorted(Hundreds.items(), key=lambda x: len(x[0]))):
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    for rom, dig in reversed(sorted(Thousands.items(), key=lambda x: len(x[0]))):
        if rom in roman_string:
            equiled_digit += dig
            roman_string = roman_string[:-len(rom)]
            break
    return (equiled_digit)

print(roman_to_int("XXXIX"))

