#!/usr/bin/python3

vals = (1, 2, 3, 4, 5)
print(vals[0])
print(f'there are {len(vals)} elemnts in tuple')

for e in vals:
    print(e)

vals2 = [1, 2, 3, 4, 5]
vals2.append(6)
vals2.append(7)

print(f'there are {len(vals2)} elemnts in list')

for e in vals2:
    print(e)


dic = {'key' : 'value', 'key2' : 'value2', 'key3' : 'value3'}
for k, v in dic.items():
    print(k, v)

for k in dic.values():
    print(k)

data = {1, 2, 3, 4, 5}
print(data)