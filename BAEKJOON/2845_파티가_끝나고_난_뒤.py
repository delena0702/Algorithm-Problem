L, P = map(int, input().split())
data = list(map(int, input().split()))
for i in range(5):
    data[i] = data[i] - L * P
print(*data, sep=' ')