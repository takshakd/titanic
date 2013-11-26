import csv as csv
import numpy as np

from predict import predict

print "Writing predictions . . ."

modelfile = csv.writer(open("predictions.csv", "wb"))
testfile = csv.reader(open("test.csv", "rb"))

testfile.next()

for row in testfile:
    prediction = predict(row)
    row.insert(0, prediction)
    modelfile.writerow(row)
