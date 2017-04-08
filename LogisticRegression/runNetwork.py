from sklearn.externals import joblib

def runNetwork(logregFile = 'model.pkl', dataFile = 'testingInput.pkl',outputFile = 'testingOutput.pkl'):
	logreg = joblib.load(logregFile)
	X = joblib.load(dataFile)
	print logreg.predict(X)
	joblib.dump(logreg.predict(X),outputFile)


runNetwork()