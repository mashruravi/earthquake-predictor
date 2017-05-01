from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
import math
from datetime import date


#input variables to neural net
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
y = []

# Load training data from CSV
training_data = open('santiago.csv').readlines()

#calculate b-value
def calc_b_value(i):

	numerator = math.log10(math.e)
	magmin = 1.1
	magsum = 0
	for j in xrange(0,50):
		index = i - j
		record = training_data[index]
		magnitude = record.split(', ')[5].split("\n")[0]
		norm_magnitude = float(magnitude)
		
		magsum += norm_magnitude

	denominator = (magsum/50) - magmin
	return (numerator/denominator)

#calculate x6


for x in xrange(70, len(training_data) - 5):
	
	# Calculate inputs x1...x5
	x1.append(calc_b_value(x) - calc_b_value(x-4))
	x2.append(calc_b_value(x-4) - calc_b_value(x-8))
	x3.append(calc_b_value(x-8) - calc_b_value(x-12))
	x4.append(calc_b_value(x-12) - calc_b_value(x-16))
	x5.append(calc_b_value(x-16) - calc_b_value(x-20))

	# Calculate input x6
	max_mag = 0
	for z in xrange(1, x):
		prev = training_data[x - z]

		# Check if date of prev record is within 7 days
		curr_record = training_data[x].split(', ')
		curr_date = date(int(curr_record[0]), int(curr_record[1]), int(curr_record[2]))

		prev_record = prev.split(', ')
		prev_date = date(int(prev_record[0]), int(prev_record[1]), int(prev_record[2]))

		# Check if previous record is within 7 days
		if (curr_date - prev_date).days <= 7:
			mag = float(prev_record[5].split('\n')[0])
			if mag > max_mag:
				max_mag = mag

		else:
			break

	# end for

	x6.append(max_mag)

	# calculate input x7
	# print str(x) + ' - ' + str(math.pow(10, -3 * calc_b_value(x)))	
	# print x
	x7.append(math.pow(10, -3 * calc_b_value(x)))

	# get the output value
	max_mag = 0
	for i in xrange(1,6):
		record = training_data[x + i].split(', ')
		mag = float(record[5].split('\n')[0])

		if mag > max_mag:
			max_mag = mag

	# end for
	y.append(max_mag)

# end for


# Make CSV of training vectors
tv = []
training_vectors = open('training_vectors.csv', 'w')
for i in xrange(0,len(x1)):
	training_vectors.write(str(x1[i]) + ',' + str(x2[i]) + ',' + str(x3[i]) + ',' + str(x4[i]) + ',' + str(x5[i]) + ',' + str(x6[i]) + ',' + str(x7[i]) + ',' + str(y[i]) + '\n')