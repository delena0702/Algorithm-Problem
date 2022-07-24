N, M = map(int, input().split())
data = [input() for _ in range(N)]

count = [0, 0]
for i in range(N):
    if data[i].count('X') == 0:
        count[0] = count[0] + 1

for i in range(M):
    if list(map(lambda x: x[i], data)).count('X') == 0:
        count[1] = count[1] + 1

print(max(count))