
weight, alpha, goal_pred, input = 2.0, 0.1, 0.8, 1.1

error = 1
while (error > 0.00000000001):
	print("-------\nWeight:", str(weight))
	pred = input * weight
	error = (pred - goal_pred) ** 2
	delta = pred - goal_pred
	weight_delta = delta * input
	weight -= weight_delta * alpha
	print("Error:", str(error), " Prediction:", str(pred))
	print("Delta:", str(delta), " Weight delta:", str(weight_delta))
