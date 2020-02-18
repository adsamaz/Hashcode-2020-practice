
def knapsack(n, numbers):
    if n <= 0:
        return 0
    elif len(numbers) == 0:
        return 0
    elif n - numbers[0] < 0:
        return knapsack(n, numbers[1:])
    else:
        return max(knapsack(n - numbers[0], numbers[1:]) + numbers[0], knapsack(n, numbers[1:]))

filename = "c_medium.in"
f = open("inputs/"+filename, "r")
data = f.readline().split(" ")
M = int(data[0])
N = int(data[1])
pizzas = [int(x) for x in f.readline().split(" ")]
print("max:", M, "number of pizzas:", N)
print(knapsack(M, pizzas))

