# simple example

def neural_network(input, weight):
    prediction = round(input * weight, 3)
    return prediction

number_of_toes = [8.5, 9.5, 10, 9]
weight = 0.1
for input in number_of_toes:
    print("Prediction for", input, ":", neural_network(input, weight))

# for several parameters

def neural_network_several_(input, weights):
    prediction = w_sum(input, weights)
    return prediction

def w_sum(input, weights):
    assert(len(input) == len(weights))

    output = 0
    for i in range(len(input)):
        output += (input[i] * weights[i])
    return round(output, 5)

toes = [8.5, 9.5, 9.9, 9.0]
wins = [0.65, 0.8, 0.8, 0.9]
funs = [1.2, 1.3, 0.5, 1.0]

weights = [0.1, 0.2, 0.0]

for input in zip(toes, wins, funs):
    print("Prediction for", *input, ":", neural_network_several_(input, weights))
