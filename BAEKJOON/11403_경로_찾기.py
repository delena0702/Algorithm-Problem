import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [data[i][:] for i in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            dp[j][k] = max(dp[j][k], dp[j][i] * dp[i][k])

for arr in dp:
    print(*arr, sep=' ')
