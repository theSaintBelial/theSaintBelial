import numpy as np

X = np.random.normal(1, 10, (1000, 50))

m = np.mean(X, 0)
std = np.std(X, 0)

X_norm = ((X - m) / std)

Z = np.array([
	[4, 5, 0],
	[1, 9, 3],
	[5, 1, 1],
	[3, 3, 3],
	[9, 9, 9],
	[4, 7, 1],
])

r = np.sum(Z, 1)

A = np.eye(3)
B = np.eye(3)

AB = np.hstack((A, B))

print(AB)
