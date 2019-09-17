#!/usr/bin/env python

import csv
import sys
import statistics

file_name = sys.argv[1]
data = []

with open(file_name, 'r') as f:

    reader = csv.reader(f)

    for row in reader:
        for e in row:
            data.append(int(e.strip()))
            
print(data)
print(len(data))
print(min(data))
print(max(data))
print(statistics.mean(data))
print(statistics.median(data))

positive = [num for num in data if num > 0]
negative = [num for num in data if num < 0]
zeroes = [num for num in data if num == 0]

print(positive)
print(negative)
print(zeroes)
