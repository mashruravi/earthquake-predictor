from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from pybrain.tools.customxml.networkwriter import NetworkWriter

import sys
import pickle
import new_b_vals

epochs = int(sys.argv[1])

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


training_dataset = open('./pystuff/training_vectors_santiago.csv').readlines()

for line in training_dataset:
	x = line.split(",")
	ds.addSample((x[0],x[1],x[2],x[3],x[4],x[5],x[6]), (x[7],))

error = 0
trainer = BackpropTrainer(n, ds)
for x in xrange(1, epochs):
	# print(trainer.train())
	error = trainer.train()

f = open('./pystuff/err_santiago', 'wb')
pickle.dump(error, f)

NetworkWriter.writeToFile(n, "./pystuff/spec_santiago.xml")
print error
sys.stdout.flush()