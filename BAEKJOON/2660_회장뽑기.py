import sys
def input(): return sys.stdin.readline().strip()


N = int(input())

dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    dp[a][b] = dp[b][a] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

mins = list(map(lambda x: max(1, *x[1:]), dp))
minimum = min(mins)
print(minimum, mins.count(minimum))
for i in range(1, N + 1):
    if mins[i] == minimum:
        print(i, end=' ')
print()
