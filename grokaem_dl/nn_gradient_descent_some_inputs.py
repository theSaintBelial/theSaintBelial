
import numpy as np

weights = [0.1, 0.2, -.1]

def neural_network(input, weights):
	pred = np.dot(input, weights)
	return pred

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

win_or_lose_binary = np.array([1, 1, 0, 1])

true = win_or_lose_binary[0]

input = np.array([toes[0], wlrec[0], nfans[0]])

alpha = 0.01

while True:
	pred = neural_network(input, weights)

	error = (pred - true) ** 2

	if abs(pred - true) < 0.0000000000000001:
		break

	delta = (pred - true)

	weight_deltas = delta * input

	print("Pred:", pred, " Error:", error)

	for i in range(len(weights)):
		weights[i] -= alpha * weight_deltas[i]

	print("Weights:", *weights, end=' ')
	print("Weight Deltas:", *weight_deltas)



