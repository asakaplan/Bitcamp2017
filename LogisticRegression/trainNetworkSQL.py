from sklearn import linear_model, preprocessing
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score
from sklearn.metrics import matthews_corrcoef, confusion_matrix
import numpy
import pickle
from mysql.connector import (connection)
from random import random
cnx = connection.MySQLConnection(user="root", password="fuck", database='people')
cursor = cnx.cursor()
bigTableName = "people"
badness = "badness"
# Load Data
def trainNetwork(inputFile = 'trainingInput.pkl',expectedOutputFile = 'trainingOutput.pkl', modelOutputFile = 'model.pkl'):
	X = []
	Y = []
	threshold = 4.0
	NOISE_BAD = 0.3
	NOISE_GOOD =0.01
	weights = [1.0, 0.0, 2.0, 5.0,0.5,1.0,2.0,1.0,0.5] #['hasBankrupt', 'hasBond', 'hasCivilJudc', 'hasCriminal', 'hasCustComp', 'hasInvstgn', 'hasJudgment', 'hasRegAction', 'hasTermination']
	isBad = []
	cursor.execute("SELECT * FROM %s"%bigTableName)
	Y = []#joblib.load('../isBad.pic')
	for i, val in enumerate(cursor.fetchall()):
		unbuffered = bin(val[3])[2:]
		buffered = ("0"*(9-len(unbuffered))+unbuffered)
		a =  [float(a=="1") for a in buffered]
		outp = sum(weights[j]*a[j] for j in range(len(weights)))
		if outp>=threshold:
				Y.append(random()>NOISE_BAD)
		else:
				Y.append(random()<NOISE_GOOD)
		if len(buffered)!=9:
			print buffered, unbuffered, a
		X.append(tuple(a))


	X = preprocessing.normalize(X, norm='l2')


	# Create Model
	logreg = linear_model.LogisticRegression(C=1e5)
	scores = cross_val_score(logreg, X, Y, cv=5)
	#print(scores)
	logreg.fit(X, Y)
	#print X[:10]
	res = logreg.predict_proba(X)[:,1]

	cursor.execute("SELECT * FROM %s"%bigTableName)
	for i, val in enumerate(cursor.fetchall()):
		print "UPDATE %s SET `%s`=%.5f WHERE `pk`=%d"%(bigTableName,badness,res[i],val[0])
		cursor.execute("UPDATE %s SET `%s`=%.5f WHERE `pk`=%d"%(bigTableName,badness,res[i],val[0]))
	cnx.commit()
	cursor.close()
	cnx.close()
trainNetwork()
