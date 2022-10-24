import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

answer = 0
for i in range(N * M):
    y, x = divmod(i, M)
    if data[y][x] == '.':
        continue
    answer += 1

    if data[y][x] == '-':
        for j in range(x, M):
            if data[y][j] != '-':
                break
            data[y][j] = '.'
    else:
        for j in range(y, N):
            if data[j][x] != '|':
                break
            data[j][x] = '.'
print(answer)