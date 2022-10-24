import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

dp = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx, dy = 1, -1
for i in range(M + N - 1):
    x, y = max(i - N + 1, 0), min(i, N - 1)

    dp[y][x][0] = arr[y][x]

    while True:
        x += dx
        y += dy

        if not 0 <= x < M:
            break
        if not 0 <= y < N:
            break
        if arr[y][x]:
            dp[y][x][0] = dp[y - dy][x - dx][0] + 1

dx, dy = -1, -1
for i in range(M + N - 1):
    x, y = min(i, M - 1), min(N + M - i - 2, N - 1)
    dp[y][x][1] = arr[y][x]

    while True:
        x += dx
        y += dy

        if not 0 <= x < M:
            break
        if not 0 <= y < N:
            break
        if arr[y][x]:
            dp[y][x][1] = dp[y - dy][x - dx][1] + 1

answer = 0
for i in range(N):
    for j in range(M):
        for k in range(answer + 1, min(dp[i][j]) + 1):
            s = k - 1
            if dp[i + s][j - s][1] >= k and dp[i + s][j + s][0] >= k:
                answer = max(answer, k)

print(answer)