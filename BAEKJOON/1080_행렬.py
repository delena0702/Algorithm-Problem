def transform(x, y):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            data[i][j] = '1' if data[i][j] == '0' else '0'
    return

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
target = [input() for _ in range(N)]

answer = 0
for i in range(N - 2):
    for j in range(M - 2):
        if data[i][j] != target[i][j]:
            transform(j, i)
            answer = answer + 1

for idx in range(N * M):
    i, j = divmod(idx, M)
    if data[i][j] != target[i][j]:
        print(-1)
        break
else:
    print(answer)