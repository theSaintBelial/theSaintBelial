
import numpy as np

# main function
def neural_network(input: list, weights: list) -> list:
	return vector_mat_mul(input, weights)

# vector * matrix
def vector_mat_mul(input, weights):
	assert(len(input) == len(weights))

	result = [0] * len(weights)

	for i in range(len(input)):
		result[i] += w_sum(input, weights[i])
	return result

# DOT function
def w_sum(a, b):
	assert(len(a) == len(b))

	result = 0
	for i in range(len(a)):
		result += a[i] * b[i]
	return result

def outer_prod(vec_a, vec_b):
	out = [[0] * len(vec_a) for i in range(len(vec_b))]
	for i in range(len(vec_a)):
		for j in range(len(vec_b)):
			out[i][j] = vec_a[i]*vec_b[j]
	return out

# weights for toes, % wins, fans
weights = [	[0.1, 0.1, -0.3], # injuries?
			[0.1, 0.2, 0.0], # win?
			[0.0, 1.3, 0.1]	] # sadness?

# inputs for 4 teams
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# real things for 4 teams
injuries = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sadness = [0.1, 0.0, 0.1, 0.2]

# input data for 1st team
input = [toes[0], wlrec[0], nfans[0]]

# what rly happened for 1st team
true = [injuries[0], win[0], sadness[0]]

# start position
error = [0, 0, 0]
delta = [0, 0, 0]

alpha = 0.01

# while True:
for i in range(5):
	pred = neural_network(input, weights)

	for i in range(len(true)):
		error[i] = (pred[i] - true[i]) ** 2
		delta[i] = pred[i] - true[i]

	print("Preds:", *pred, " Errors:", *error)

	# check accuracy
	# trigger = 0
	# for i in error:
	# 	if i < 0.000000001:
	# 		trigger += 1
	# if trigger == len(error):
	# 	break

	weight_deltas = outer_prod(input, delta)

	for i in range(len(weights)):
		for j in range(len(weights[i])):
			weights[i][j] -= alpha * weight_deltas[i][j]

	print("Weights:", *weights, " Weight deltas:", *weight_deltas)
