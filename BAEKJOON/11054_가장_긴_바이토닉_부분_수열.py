import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)

for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if data[i] > data[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

print(max(map(sum, dp)) - 1)