
import numpy as np

a = np.array([0, 1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.array([
	[0, 1, 2, 3],
	[4, 5, 6, 7]])
d = np.zeros((2, 4)) # zero filled matrix 2x4
e = np.random.rand(2, 5) # random numbers from 0 to 1 2x5

print(a)
print(b)
print(c)
print(d)
print(e)

# kek, remember about matrix*matrix rules

a = np.zeros((2, 4))
print(a)
b = np.zeros((4, 3))
print(b)

c = a.dot(b)
print(c.shape)

d = np.zeros((5, 4)).T # T for transposing
e = np.zeros((5, 6))

f = d.dot(e)
print(f.shape)
