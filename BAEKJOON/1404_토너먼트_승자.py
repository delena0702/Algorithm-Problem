import sys
def input(): return sys.stdin.readline().strip()

arr = list(map(int, input().split()))

cnt = 0
data = [[0] * 8 for _ in range(8)]
for i in range(8):
    for j in range(i + 1, 8):
        data[i][j] = arr[cnt]
        cnt += 1

arr = [[0] * 8 for _ in range(8)]

for i in range(4, 8):
    a, b = 2 * (i - 4), 2 * (i - 4) + 1
    arr[i][a] = data[a][b]
    arr[i][b] = 100 - data[a][b]

for i in range(3, 0, -1):
    a, b = 2 * i, 2 * i + 1
    for j in range(8):
        for k in range(j + 1, 8):
            cnt = arr[a][j] * arr[b][k] + arr[a][k] * arr[b][j]
            arr[i][j] += cnt * data[j][k]
            arr[i][k] += cnt * (100 - data[j][k])

    for j in range(8):
        arr[i][j] /= 10000

for i in range(8):
    print(f"{arr[1][i] / 100:.11f} ", end='')