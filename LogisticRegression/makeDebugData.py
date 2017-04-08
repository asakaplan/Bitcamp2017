from sklearn import  datasets 
from sklearn.externals import joblib
from sklearn import linear_model, preprocessing

# Import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # We only take the first two features.
print X
Y = iris.target

joblib.dump(X, 'trainingInput.pkl') 
X = preprocessing.normalize(X, norm='l2')
joblib.dump(X, 'testingInput.pkl') 
joblib.dump(Y, 'trainingOutput.pkl')