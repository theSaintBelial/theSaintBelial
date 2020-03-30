
weight = 0.5
input = 0.5

goal_pred = 0.8
print("Real deal:", goal_pred)

pred = input * weight
print("Prediction of our NN:", pred)

error = (pred - goal_pred) ** 2

print("Error RMS:", round(error, 4))


# cold/hot method

weight = 0.5
weight_step = 0.001

input = 0.5
goal_pred = 0.8

for i in range(1101):
	pred = round(input * weight, 10)
	error = round((pred - goal_pred) ** 2, 10)

	print("Error:", str(error), " Prediction:", round(pred, 10))

	up_pred = input * (weight + weight_step)
	up_error = (up_pred - goal_pred) ** 2

	dn_pred = input * (weight - weight_step)
	dn_error = (dn_pred - goal_pred) ** 2

	if (dn_error < up_error):
		weight -= weight_step
	if (dn_error > up_error):
		weight += weight_step
