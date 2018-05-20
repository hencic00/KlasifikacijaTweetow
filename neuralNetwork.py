import json
import pickle
from sklearn.neural_network import MLPClassifier

def loadDataSet(path):
	with open(path, "r") as f:
		data = json.loads(f.read())
		intputVectors, classifications = map(list, zip(*data))
		return intputVectors, classifications

def teachNNetwork(inputVector, classifications, saveToDisk=False):
	mlp = MLPClassifier(verbose=True, solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(len(inputVector[0])), random_state=1)
	mlp.fit(inputVector, classifications) # X of size (n_samples, n_features),  y of size (n_samples,) holding target values
	
	if saveToDisk:
		filename = './dataSets/NNcoeficients.sav'
		pickle.dump(mlp, open(filename, 'wb'))
	return mlp

def loadNNetwork():
	return pickle.load(open('./dataSets/NNcoeficients.sav', 'rb'))

def testNNetwork(mlp, inputVector, classifications):
	testResults = mlp.predict(inputVector).tolist()
	similarity = 0
	for i in range(len(classifications)):
		if (testResults[i] == classifications[i]):
			# print("{}~{}".format(testResults[i], classifications[i]))
			similarity += 1

	print ("Success rate: {}".format(similarity / float(len(testResults))))

def NNetworkMain():
 	#teachNNetwork(*loadDataSet("./dataSets/trainSet.json"), saveToDisk=True); #saveToDisk=True
	mlp = loadNNetwork()
	testNNetwork(mlp, *loadDataSet("./dataSets/testSet.json"))

NNetworkMain()