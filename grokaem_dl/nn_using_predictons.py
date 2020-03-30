
# существуют также нейросети, реализованнные с помоью прогнозирования прогнозов:
# 	когда одной матрицы недостаточно, чтобы получить необходимые прогнозы и вводят
# 	дополнительное промежуточное создение прогноза
#		входные - прогноз (скрытый) - прогноз (выходной)

import numpy as np

# Columns: 1) plays  2)wins %  3) fans

ih_wgt = np.array([
	[0.1, 0.2,-0.1],	# hid[0]
	[-0.1, 0.1, 0.9],	# hid[1]
	[0.1, 0.4, 0.1]		# hid[2]
]).T

# hid[0] hid[1] hid[2]

hp_wgt = np.array([
	[0.3, 1.1, -0.3],	# injuries
	[0.1, 0.2, 0.0],	# victory
	[0.0, 1.3, 0.1]		# sadness
]).T

weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
	hid = np.dot(input, weights[0])
	predictions = np.dot(hid, weights[1])
	return predictions

toes = np.array([8.5, 9.5, 9.9, 9.0])
wins = np.array([0.65, 0.8, 0.8, 0.9])
fans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wins[0], fans[0]])

pred = neural_network(input, weights)

print("Predictions:")
for i in pred:
	print(round(i, 3), end=' ')
