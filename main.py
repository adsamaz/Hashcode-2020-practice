import time

def knapsack(n, numbers):
    l = len(numbers)
    if n <= 0:
        T[n][l] = 0
        return 0
    elif len(numbers) == 0:
        T[n][l] = 0
        return 0
    elif n - numbers[0] < 0:
        if T[n][l] == 0:
            T[n][l] = knapsack(n, numbers[1:])
    else:
        if T[n][l] == 0:
            T[n][l] = max(knapsack(n - numbers[0], numbers[1:]) + numbers[0], knapsack(n, numbers[1:]))
    return T[n][l]


filename = "c_medium.in"
f = open("inputs/"+filename, "r")
data = f.readline().split(" ")
M = int(data[0])
N = int(data[1])
pizzas = [int(x) for x in f.readline().split(" ")]

T = [[0 for _ in range(len(pizzas) + 1)] for _ in range(M+1)]

print("max:", M, "number of pizzas:", N)


start = time.time()
print(knapsack(M, pizzas))
end = time.time()
print("Running time:", end - start)
