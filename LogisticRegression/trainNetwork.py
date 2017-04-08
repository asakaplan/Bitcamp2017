from sklearn import linear_model, preprocessing
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score
from sklearn.metrics import matthews_corrcoef, confusion_matrix
import pickle

# Load Data
def trainNetwork(inputFile = 'trainingInput.pkl',expectedOutputFile = 'trainingOutput.pkl', modelOutputFile = 'model.pkl'):
	a=pickle.load(open("../consolodatedOutput.pic","r"))
	X = [b[2] for b in a]
	#X = joblib.load('trainingInput.pkl')
	Y = joblib.load('../isBad.pic')

	# Feature Scaling / Normalization
	X = preprocessing.normalize(X, norm='l2')


	# Create Model
	logreg = linear_model.LogisticRegression(C=1e5)
	scores = cross_val_score(logreg, X, Y, cv=5)
	print(scores)
	logreg.fit(X, Y)
	print X[:10]
	print(confusion_matrix(Y,logreg.predict(X)))
	print(matthews_corrcoef(Y,logreg.predict(X)))
	# Save Model
	joblib.dump(logreg, 'model.pkl')

	# Update Training Input
	joblib.dump(X,'trainingInput.pkl')

trainNetwork()
