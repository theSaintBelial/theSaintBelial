
import numpy as np

weights = np.array([0.1, 0.2, 0])

def neural_network(input, weights):
    return round(input.dot(weights), 5) # говно-реализация
    # return round(np.dot(input, weights), 5)

toes = np.array([8.5, 9.5, 9.9, 9.0])
wins = np.array([0.65, 0.8, 0.8, 0.9])
fans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wins[0], fans[0]])
print(neural_network(input, weights))


