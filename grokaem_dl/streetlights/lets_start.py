
import numpy as np

streetlights = np.array([
	[1, 0, 1],
	[0, 1, 1],
	[0, 0, 1],
	[1, 1, 1],
	[0, 1, 1],
	[1, 0, 1]
])

walk_or_stop = np.array([
	[0],
	[1],
	[0],
	[1],
	[1],
	[0]
])

alpha = 0.1

weights = np.array([0.5, 0.48, -0.7])

for i in range(1000):
	error_for_all_lights = 0
	for row in range(len(walk_or_stop)):
		input = streetlights[row]
		goal_prediction = walk_or_stop[row]

		prediction = round(np.dot(input, weights), 4)

		error = round(float((goal_prediction - prediction) ** 2), 5)
		error_for_all_lights += error

		delta = prediction - goal_prediction
		weights = weights - (alpha * delta * input)

test_input = [1, 0, 1]

test_prediction = abs(round(np.dot(test_input, weights)))

print("Input:", *test_input)

print("Test prediction:", test_prediction)

print("Weights:", *weights)
