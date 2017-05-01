from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
import math
from datetime import date

def get_b_vals():
	#input variables to neural net
	x1 = 0
	x2 = 0
	x3 = 0
	x4 = 0
	x5 = 0
	x6 = 0
	x7 = 0

	# Load training data from CSV
	training_data = open('./pystuff/santiago.csv').readlines()

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


	x = len(training_data) - 1
		
	# Calculate inputs x1...x5
	x1 = calc_b_value(x) - calc_b_value(x-4)
	x2 = calc_b_value(x-4) - calc_b_value(x-8)
	x3 = calc_b_value(x-8) - calc_b_value(x-12)
	x4 = calc_b_value(x-12) - calc_b_value(x-16)
	x5 = calc_b_value(x-16) - calc_b_value(x-20)

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

	x6 = max_mag

	# calculate input x7
	# print str(x) + ' - ' + str(math.pow(10, -3 * calc_b_value(x)))	
	# print x
	x7 = math.pow(10, -3 * calc_b_value(x))


	return [x1, x2, x3, x4, x5, x6, x7]