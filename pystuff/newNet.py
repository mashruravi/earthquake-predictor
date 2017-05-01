from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(7,1)

n = FeedForwardNetwork()

inLayer = LinearLayer(7)
hiddenLayer = SigmoidLayer(15)
outLayer = LinearLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer,hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()


training_dataset = open('training_vectors.csv').readlines()

for line in training_dataset:
	x = line.split(",")
	ds.addSample((x[0],x[1],x[2],x[3],x[4],x[5],x[6]), (x[7],))

trainer = BackpropTrainer(n, ds)
print(trainer.trainUntilConvergence())