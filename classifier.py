import pickle
from random import random
a=pickle.load(open("consolodatedOutput.pic","r"))
print "Loaded data"
print a[1]
exit(0)
threshold = 4.0
NOISE_BAD = 0.3
NOISE_GOOD =0# 0.001
weights = [1.0, 0.0, 2.0, 5.0,0.5,1.0,2.0,1.0,0.5] #['hasBankrupt', 'hasBond', 'hasCivilJudc', 'hasCriminal', 'hasCustComp', 'hasInvstgn', 'hasJudgment', 'hasRegAction', 'hasTermination']
isBad = []
for i in range(len(a)):
    outp = sum(weights[j]*a[i][2][j] for j in range(len(weights)))
    if outp>=threshold:
        isBad.append(random()>NOISE_BAD)
    else:
        isBad.append(random()<NOISE_GOOD)
print sum(isBad), len(isBad)
pickle.dump(isBad, open("isBad.pic","w"))
