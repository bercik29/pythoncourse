#!/usr/bin/env pyhon

import csv

fi = open('number.csv', 'r')
_sum = 0

with fi:
    read = csv.DictReader(fi)
    print(read.fieldnames)

    f1, f2, f3 = read.fieldnames

    for row in read:
        print(row[f1], row[f2], row[f3])


fi2 = open('number2.csv', 'w')


num = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

with fi2:
    fnames = ['one','two','three','four','five','six']
    writer = csv.DictWriter(fi2, fieldnames=fnames)
    writer.writeheader()
    writer.writerows(num)
#    for row in num:
#        writer.writerow(row)