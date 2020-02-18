f = open("inputs/a_example.in", "r")
data = f.readline().split(" ")
M = data[0]
N = data[1]
pizzas = map(lambda x: int(x), f.readline().split(" "))
print(list(pizzas))
