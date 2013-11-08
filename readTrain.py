import csv as csv
import numpy as np

fp = csv.reader(open('train.csv', 'rb'))
header = fp.next()

data = []
for row in fp:
	data.append(row)

data = np.array(data)

Npassengers = np.size(data[0::,0].astype(np.float))
Nsurvivors  = np.sum(data[0::,0].astype(np.float))
percentage = Nsurvivors/Npassengers;

womenIdx = data[0::,4] == "female"
menIdx   = data[0::,4] == "male"

womenOnboard = data[womenIdx, 0].astype(np.float)
menOnboard   = data[menIdx, 0].astype(np.float)

womenSurvivors = data[womenIdx, 1] == "1"
menSurvivors   = data[menIdx, 1] == "1"

percentageWomenSurvivors = np.sum(womenOnboard) / np.size(womenOnboard)
percentageMenSurvivors   = np.sum(menOnboard) / np.size(menOnboard)

print 'Percentage of women survivors = %s' % percentageWomenSurvivors
print 'Percentage of men survivors   = %s' % percentageMenSurvivors

