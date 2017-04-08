import pickle
a=pickle.load(open("consolodatedOutput.pic","r"))
print "Loaded data"
threshold = 4.0
weights = [1.0, 0.0, 2.0, 5.0,0.5,1.0,2.0,1.0,0.5] #['hasBankrupt', 'hasBond', 'hasCivilJudc', 'hasCriminal', 'hasCustComp', 'hasInvstgn', 'hasJudgment', 'hasRegAction', 'hasTermination']
isBad = []
for i in range(len(a)):
    outp = sum(weights[j]*a[i][2][j] for j in range(len(weights)))
    isBad.append(outp>=threshold)
print sum(isBad), len(isBad)
pickle.dump(isBad, open("isBad.pic","w"))
