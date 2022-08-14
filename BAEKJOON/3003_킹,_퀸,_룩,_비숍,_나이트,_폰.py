sample = [1, 1, 2, 2, 2, 8]
data = list(map(int, input().split()))
print(*list(map(lambda x: sample[x[0]] - x[1], enumerate(data))))