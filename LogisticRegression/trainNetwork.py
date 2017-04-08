from sklearn import linear_model, preprocessing
from sklearn.externals import joblib


# Load Data
def trainNetwork(inputFile = 'trainingInput.pkl',expectedOutputFile = 'trainingOutput.pkl', modelOutputFile = 'model.pkl'):
	X = joblib.load('trainingInput.pkl')
	Y = joblib.load('trainingOutput.pkl')

	# Feature Scaling / Normalization
	X = preprocessing.normalize(X, norm='l2')


	# Create Model
	logreg = linear_model.LogisticRegression(C=1e5)
	logreg.fit(X, Y)

	# Save Model
	joblib.dump(logreg, 'model.pkl') 

	# Update Training Input
	joblib.dump(X,'trainingInput.pkl')

trainNetwork()