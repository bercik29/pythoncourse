#!/usr/bin/python3

nums = { 1, 2, 2, 2, 3, 4 }

nums.add(5)
nums.remove(2)



print(type(nums))
print(nums)

seasons = ["spring", "summer", "autumn", "winter"]

myset = set(seasons)

print(myset)

words = { "spring", "table", "cup", "bottle", "coin" }

word = 'cup'

if (word in words):
    print("{0} is present in the set".format(word))
else:
    print("{0} is not present in the set".format(word))    

word = 'tree'

if (word not in words):
    print("{0} is not present in the set".format(word))
else:
    print("{0} is present in the set".format(word)) 


nums = { 21, 11, 42, 29, 22, 71, 18 }

print(nums)

print("Number of elements: {0}".format(len(nums)))
print("Minimum: {0}".format(min(nums)))
print("Maximum: {0}".format(max(nums)))
print("Sum: {0}".format(sum(nums)))

print("Sorted elements:")

print(sorted(nums))

words = { "spring", "table", "cup", "bottle", "coin" }

words.add("coffee")

print(words)

words2 = { "car", "purse", "wind" }
words3 = { "nice", "prime", "puppy" }

words.update(words2, words3)

print(words)

set1 = { 'a', 'b', 'c', 'c', 'd' }
set2 = { 'a', 'b', 'x', 'y', 'z' }

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1.intersection(set2))
print("union:", set1.union(set2))
print("difference:", set1.difference(set2))
print("symmetric difference:", set1.symmetric_difference(set2))

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1 & set2)
print("union:", set1 | set2)
print("difference:", set1 - set2)
print("symmetric difference:", set1 ^ set2)

set1 = { 'a', 'b', 'c', 'd', 'e' }
set2 = { 'a', 'b', 'c' }
set3 = {'x', 'y', 'z' }

if (set2.issubset(set1)):
    print("set2 is a subset of set1")
    
if (set1.issuperset(set2)):
    print("set1 is a superset of set2")    
    
if (set2.isdisjoint(set3)):
    print("set2 and set3 have no common elements")   

    s1 = frozenset(('blue', 'green', 'red'))
    # s1.add('brown')