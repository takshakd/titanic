import csv as csv
import numpy as np

print "Writing predictions . . ."

modelfile = csv.writer(open("predictions.csv", "wb"))
testfile = csv.reader(open("test.csv", "rb"))

testfile.next()

for row in testfile:
    if row[3] == "female":
        row.insert(0, "lives")
        modelfile.writerow(row)
    else:
        row.insert(0, "dies")
        modelfile.writerow(row)
