#!/usr/bin/env pyhon

val = 0

for i in range(1, 101, 1):
   val += i

print(f"sucet 1..100 je: {val}") 

val = sum(range(101))
print(f"sucet 1..100 je: {val}") 

citam = input('zadaj slovo: ')
if len(citam) == 0:
    print(f'slovo {citam} je bez znakov')
elif len(citam) == 1:
    print(f'slovo {citam} ma {len(citam)} znak')
elif len(citam) < 4:
    print(f'slovo {citam} ma {len(citam)} znaky')
else:
    print(f'slovo {citam} ma {len(citam)} znakov')

ntica = (0, 5, 6, 8, 1, 10, -4, -2, 3)
print(f' maximum ntice {ntica} je {max(ntica)}')
print(f' minimum ntice {ntica} je {min(ntica)}')
print(f' pocet prvkov ntice {ntica} je {len(ntica)}')
print(f' suma ntice {ntica} je {sum(ntica)}')
print(f' prvy clen ntice {ntica} je {ntica[0]}')
print(f' posledny clen ntice {ntica} je {ntica[-1]}')

valueMin = ntica[0]
valueMax = ntica[0]
for i in ntica: # i odkazuje na hodnotu nie poziciu, for v tomto pripade automaticky prechadza cez prvky tuple
    if i < valueMin:
        valueMin = i
    if i > valueMax:
        valueMax = i

print(f'najdene cez for loop minimum je {valueMin} a maximum je {valueMax}')

valueMin = ntica[0]
valueMax = ntica[0]
i = 0
while i <= len(ntica)-1:
    if ntica[i] < valueMin:
        valueMin = ntica[i]
    if ntica[i] > valueMax:
        valueMax = ntica[i]
    i += 1

print(f'najdene cez while loop minimum je {valueMin} a maximum je {valueMax}')

x = sorted(ntica)
xx = sorted(ntica, reverse = True)

print(f'sorted ntica {x}')
print(f'reverse sorted ntica {xx}')