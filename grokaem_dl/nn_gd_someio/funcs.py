
import numpy as np

# input: list
# weights: 2-dim matrix
def neural_network(input, weights):
	output = np.zeros(len(weights))

	for i in range(len(weights)):
		output[i] = round(np.dot(input, weights[i]), 5)
	return output

def delta(true, prediction):
	deltas = np.zeros(len(true))

	for i in range(len(true)):
		deltas[i] = prediction[i] - true[i]
	return deltas

def error(delta):
	errors = np.zeros(len(delta))

	for i in range(len(delta)):
		errors[i] = round(delta[i] ** 2, 5)
	return errors

def weight_deltas(input, deltas):
	w_deltas = np.zeros((len(input), len(input)))

	for i in range(len(input)):
		for j in range(len(input)):
			w_deltas[i][j] = round(input[i] * deltas[j], 5)
	return w_deltas

def weights_balance(weights, weight_deltas):
	return weights - weight_deltas * 0.0001
