#!/usr/bin/env pyhon

vals = '1@2@3@4@5@6@7@8@9@10'

splitted = vals.split('@')

print(splitted)

suma = 0

for i in splitted:
    suma += int(i)

print(suma)

alpha = 0
digits = 0
other = 0
spaces = 0
numlines = 0

with open('data.txt') as f:
    for lines in f:    
        while lines:
            lines = f.readline()
            print(lines)
            numlines = +1
            for line in lines:
                for character in line:
                    if character.isalpha():
                        alpha += 1
                    elif character.isdigit():
                        digits += 1
                    elif character.isspace():
                        spaces += 1
                    else:
                        other += 1
        if not lines:
            break

print(f'Alphanumeric symbols: {alpha}')
print(f'Spaces: {spaces}')
print(f'Number: {digits}')
print(f'Other: {other}') 
print(f'Lines: {numlines}')