
import numpy as np
import funcs as f

# weights for toes, % wins, fans
weights = np.array([[0.1, 0.2, 0.2], # injuries?
			[0.1, 0.2, 0.1], # win?
			[0.0, 1.3, -0.1]]) # sadness?

# inputs for 4 teams
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([0.0, 1.3, 0.5, 1.0])

# real things for 4 teams
injuries = np.array([0.3, 0.0, 0.0, 0.1])
win = np.array([1, 1, 0, 1])
sadness = np.array([0.1, 1.0, 0.1, 0.2])

# input data for 1st team
input = np.array([toes[0], wlrec[0], nfans[0]])

# what rly happened for 1st team
true = np.array([injuries[0], win[0], sadness[0]])

# start position
error = np.array([0, 0, 0])
delta = np.array([0, 0, 0])

#--------------------------------------------------------------
#--------------------------------------------------------------

for i in range(1000):
	error_for_all = np.zeros(3)
	for i in range(len(toes)):
		input = np.array([toes[i], wlrec[i], nfans[i]])

		true = np.array([injuries[i], win[i], sadness[i]])

		prediction = f.neural_network(input, weights)

		delta = f.delta(true, prediction)

		error = f.error(delta)

		error_for_all += error

		weight_deltas = f.weight_deltas(input, delta)

		weights = f.weights_balance(weights, weight_deltas)

	print("Error:", *error_for_all)

print("\n----------------------------------------------------\n\nWeights:")
for i in weights:
	for j in i:
		print("%9f" % round(j, 5), end='  ')
	print()
