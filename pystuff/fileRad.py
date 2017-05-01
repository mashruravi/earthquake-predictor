import math
from datetime import date

training_data = open('santiago.csv').readlines()

def calc_b_value(i):

	numerator = math.log10(math.e)

	for j in xrange(0,50):
		index = i - j
		record = training_data[index]
		magnitude = record.split(', ')[5].split("\n")[0]
	print magnitude


calc_b_value(70)