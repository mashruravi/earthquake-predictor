from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from pybrain.tools.customxml.networkwriter import NetworkWriter

import sys
import new_b_vals

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


training_dataset = open('./pystuff/training_vectors.csv').readlines()

for line in training_dataset:
	x = line.split(",")
	ds.addSample((x[0],x[1],x[2],x[3],x[4],x[5],x[6]), (x[7],))

trainer = BackpropTrainer(n, ds)
for x in xrange(1,100):
	# print(trainer.train())
	trainer.train()

# b_vals = new_b_vals.get_b_vals()
# print(n.activate(b_vals))
# sys.stdout.flush()

NetworkWriter.writeToFile(n, "./pystuff/spec.xml")
print "Training complete"
sys.stdout.flush()