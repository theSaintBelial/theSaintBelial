
# columns: 1: games 2: win % 3: fans

weights = [
    [0.1, 0.1, -0.3], # injuries
    [0.1, 0.2, 0.0], # victory
    [0.0, 1.3, 0.1] # sadness
]

def neural_network(input: list, weights: list) -> list:
    return vector_mat_mul(input, weights)

def vector_mat_mul(input, weights):
    assert(len(input) == len(weights))

    result = [0] * len(weights)

    for i in range(len(input)):
        result[i] += w_sum(input, weights[i])
    return result


def w_sum(a, b):
    assert(len(a) == len(b))

    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return round(result, 5)

toes = [8.5, 9.5, 9.9, 9.0]
wins = [0.65, 0.8, 0.8, 0.9]
fans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wins[0], fans[0]]

for i in range(len(toes)):
    print("Result #", i + 1, sep='', end=': ')
    print(*neural_network([toes[i], wins[i], fans[i]], weights))