#!/usr/bin/env pyhon

weekend = {"Sun":"Sunday", "Mon":"Monday"}
vals = dict(one=1, two=2)

capitals = {}
capitals['svk'] = "BA"
capitals['deu'] = "Berlin"
capitals['dnk'] = "Copenhagen"

print(weekend)
print(vals)
print(capitals)

print(f'there are {format(len(capitals))} capitals in dict')
print(capitals['svk'])

capitals['svk'] = "Bratislava"
print(capitals['svk'])

# print(capitals['uk'])

print(capitals.get('uk','undefined'))

# zlucenie slovnikov

capitals.update(weekend)
print(capitals)

print(capitals.pop("Mon"))
print(capitals)

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for e in capitals.keys():
    print(capitals.get(e, 'undefined'))
    print(e in capitals)

for key in capitals:
    print(key)
    
for val in capitals.values():
    print(val)

for (k, v) in capitals.items():
    print(": ".join((k,v))) # alternative to print(f'{k}: {v}')