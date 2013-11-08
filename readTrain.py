import csv as csv
import numpy as np

print "------------------------------------"

fp = csv.reader(open('train.csv', 'rb'))
header = fp.next()

data = []
for row in fp:
	data.append(row)

data = np.array(data)

Npassengers = np.size(data[0::, 0])
Nsurvivors  = np.sum((data[0::, 1]=="1").astype(np.float))
percentage = 100*Nsurvivors/Npassengers;
print "Percentage survivors = %s" % percentage

women = (data[0::,4] == "female")
men   = (data[0::,4] == "male")

womenSurvivors = (data[women, 1] == "1").astype(np.float)
menSurvivors   = (data[men, 1] == "1").astype(np.float)

percentageWomenSurvivors = 100 * np.sum(womenSurvivors) / np.sum(women.astype(np.float))
percentageMenSurvivors   = 100 * np.sum(menSurvivors) / np.sum(men.astype(np.float))

print 'Percentage of women survivors = %s' % percentageWomenSurvivors
print 'Percentage of men survivors   = %s' % percentageMenSurvivors

print "------------------------------------"
