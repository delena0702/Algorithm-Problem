import sys
def input(): return sys.stdin.readline().strip()

N, data = int(input()), input().split()

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        if data[i] == data[N - j - 1]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)

print(N - dp[-1][-1])