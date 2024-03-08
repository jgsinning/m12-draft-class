#import pandas as pd
#
#csv = pd.read_csv('GUIDE.csv')
#print(csv)

import numpy as np

file = open('GUIDE.csv', 'r')
file.readline()

ovrs = {}
pots = {}
for i in range(21):
    ovrs[i] = []
    pots[i] = []

for i in range(257):
    line = file.readline().split('\n')[0].split(',')
    pos = int(line[0].split('-')[0])
    ovrs[pos].append(int(line[4]))
    pots[pos].append(int(line[5]))

file.close()
means = {}
quartiles = {}
stddev = {}

for i in range(21):
    ovr = ovrs[i]
    means[i] = sum(ovr) / len(ovr)
    quartiles[i] = np.quantile(ovr, [0, 0.25, 0.5, 0.75, 1])
    stddev[i] = np.std(ovr)

#print(means)
#print(quartiles)
#print(stddev)

output = open('GUIDE-ANALYZED.csv', 'w')
output.write('POSITION,MEAN,STD,LOW,Q1,MED,Q3,HIGH\n')
for i in range(21):
    output.write(f'{i},{means[i]},{stddev[i]},{quartiles[i][0]},{quartiles[i][1]},{quartiles[i][2]},{quartiles[i][3]},{quartiles[i][4]}\n')

means = {}
quartiles = {}
stddev = {}

for i in range(21):
    ovr = pots[i]
    means[i] = sum(ovr) / len(ovr)
    quartiles[i] = np.quantile(ovr, [0, 0.25, 0.5, 0.75, 1])
    stddev[i] = np.std(ovr)

output.write('POSITION,MEAN,STD,LOW,Q1,MED,Q3,HIGH\n')
for i in range(21):
    output.write(f'{i},{means[i]},{stddev[i]},{quartiles[i][0]},{quartiles[i][1]},{quartiles[i][2]},{quartiles[i][3]},{quartiles[i][4]}\n')

output.close()
