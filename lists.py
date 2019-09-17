#!/usr/bin/env pyhon

values = [1, 3, 5, -1, 2] # [list], je mozne ho menit, vymazavat, prepisat atd (na rozdiel od (tuple) )

print(len(values))
print(max(values))
print(min(values))
print(sum(values))
print(values[0])
print(values[-1])

for e in values:
    print(e, end = ' ')

print()

values[4] = 22
print(values)

values.extend(values) # vieme pridavat veci co su iterable
print(values)

values.extend(range(5)) # vieme pridavat veci co su iterable
print(values)

values.remove(values[3])
print(values)

values.remove(22)
print(values)

values.sort()
print(values)

print(values.count(2))
print(values.count(1))


# slices

print(values[1:5]) # id 1, 2, 3, 4
print(values[:5])
print(values[10:])
print(values[10::2]) # od 10 do konca so step 2
print(values[:])

print(values[-5:-1])
print(values[:-3])
print(values[-10:10])
print(values[-10:10:2]) # od -10 so step 2
print(values[::-1]) # zaporny krok na chod od konca

values.clear()
print(values)

matica = [[1, 2, 3], [3, 4, [5, 6, [7]]]] # vnorene listy

print(matica[0])
print(matica[1])

print(matica[0][0])
print(matica[0][1])
print(matica[1][0])

# print(matica[1][1][1])