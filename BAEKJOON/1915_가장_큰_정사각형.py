import sys
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
data, dp = [input() for _ in range(N)], [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            dp[i][j] = 1 if data[i][j] == '1' else 0
        elif data[i][j] == '1':
            dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
print(max([max(a) for a in dp]) ** 2)