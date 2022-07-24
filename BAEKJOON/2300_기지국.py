N = int(input())
data = sorted([list(map(int, input().split())) for _ in range(N)])
for i in range(N):
    data[i][1] = abs(data[i][1])

dp = [float('inf')] * N
dp[0] = data[0][1] * 2
for i in range(1, N):
    maximum = -1
    for j in range(i, -1, -1):
        maximum = max(maximum, data[j][1])
        cost = max(data[i][0] - data[j][0], 2 * maximum)
        dp[i] = min(dp[i], cost + (dp[j - 1] if j else 0))

print(dp[-1])