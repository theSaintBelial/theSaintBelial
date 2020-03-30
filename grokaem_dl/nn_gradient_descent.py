
weight = 0.5
goal_pred = 0.8
input = 0.5

for i in range(20):
	pred = input * weight
	error = (pred - goal_pred) ** 2
	direction_and_amount = (pred - goal_pred) * input
	weight -= direction_and_amount

	print("Error:", error, " Prediction:", pred)
