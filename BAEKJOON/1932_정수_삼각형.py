import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N):
    for j in range(i, -1, -1):
        dp[j] = max(dp[j - 1], dp[j]) + data[i][j]
print(max(dp))
