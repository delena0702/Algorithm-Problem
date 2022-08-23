n, data = int(input()), (0, 1)
for _ in range(n):
    data = (data[1], sum(data))
print(data[0])