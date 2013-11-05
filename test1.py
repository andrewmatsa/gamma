import csv
import random
import sys

f = open("C:\\test.csv", 'rt')
names = []
surnames = []
try:
    reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
    for row in reader:
        names.append(row[0])
        surnames.append(row[1])
    print names[random.randint(0, names.__len__() - 1)]
    print surnames[random.randint(0, names.__len__() - 1)]
finally:
    f.close()


