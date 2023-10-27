import re

# Polski kod pocztowy
pattern_pl = re.compile(r'^\d{2}-\d{3}$')

# Prośba o wprowadzenie kodu pocztowego
postal_code = input("Podaj kod pocztowy: ")

try:
    if not pattern_pl.match(postal_code):
        raise ValueError("Niepoprawny kod pocztowy!")
    else:
        with open('kodypocztowe.txt', 'a') as f:
            f.write(postal_code + '\n')
except ValueError as e:
    print(e)


import re

# Amerykański kod pocztowy
pattern_us = re.compile(r'^\d{5}(-\d{4})?$')

# Prośba o wprowadzenie kodu pocztowego
postal_code = input("Podaj kod pocztowy: ")

try:
    if not pattern_us.match(postal_code):
        raise ValueError("Niepoprawny kod pocztowy!")
    else:
        with open('kodypocztowe.txt', 'a') as f:
            f.write(postal_code + '\n')
except ValueError as e:
    print(e)
