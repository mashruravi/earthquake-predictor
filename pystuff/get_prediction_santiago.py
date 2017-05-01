from pybrain.tools.customxml.networkreader import NetworkReader

import new_b_vals
import sys
import pickle

net = NetworkReader.readFrom('./pystuff/spec_santiago.xml')

f = open('./pystuff/err_santiago', 'rb')
error = pickle.load(f)

accuracy = (1 - float(error)) * 100
accuracy = "%.1f" % accuracy

b_vals = new_b_vals.get_b_vals()
print str("%.2f" % net.activate(b_vals)[0]) + ':' + str(accuracy)
sys.stdout.flush()
