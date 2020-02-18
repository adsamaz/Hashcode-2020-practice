import time

def knapsack(n, numbers):
    l = len(numbers)
    if n <= 0:
        T[(n,l)] = 0
        return 0
    elif len(numbers) == 0:
        T[(n,l)] = 0
        return 0
    elif n - numbers[0] < 0:
        if not T.get((n,l)):
            T[(n,l)] = knapsack(n, numbers[1:])
    else:
        if not T.get((n,l)):
            T[(n,l)] = max(knapsack(n - numbers[0], numbers[1:]) + numbers[0], knapsack(n, numbers[1:]))
    return T[(n,l)]


filename = "c_medium.in"
f = open("inputs/"+filename, "r")
print("reading file...")
data = f.readline().split(" ")
M = int(data[0])
N = int(data[1])
pizzas = [int(x) for x in f.readline().split(" ")]
print("creating data structure...")
T = {}
print("done.")
print("max:", M, "number of pizzas:", N)
print("calculating...")

start = time.time()
print(knapsack(M, pizzas))
end = time.time()
print("Running time:", end - start)
