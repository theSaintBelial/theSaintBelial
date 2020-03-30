
# idk why i had done it

def elementwise_mult(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    
    result = []

    for i in range(len(vec_b)):
        result.append(vec_a[i] * vec_b[i])
    return result

vec_a = [i for i in range(5)]
vec_b = [i for i in range(0, -5, -1)]

print(vec_a, vec_b, sep="\n")

print("\nMult:", *elementwise_mult(vec_a, vec_b), end="\n---------------------------------------------------------\n")

def elementwise_sum(vec_a, vec_b):
    assert(len(vec_b) == len(vec_a))

    result = []
    for i in range(len(vec_a)):
        result.append(vec_a[i] + vec_b[i])
    return result

print("Sum:", *elementwise_sum(vec_a, vec_b), end="\n---------------------------------------------------------\n")

def vector_sum(vec_a):
    sum = 0

    for i in vec_a:
        sum += i
    return sum

print("Vector a sum:", vector_sum(vec_a), end="\n---------------------------------------------------------\n")

def vector_average(vec_a):
    average = 0
    for i in vec_a:
        average += i
    return average / len(vec_a)

print("Vector a average:", vector_average(vec_a), end="\n---------------------------------------------------------\n")
