N, dp = int(input()), [1] * 2
for i in range(N):
    dp = [(dp[0] + 2 * dp[1]) % 9901, (dp[0] + dp[1]) % 9901]
print(dp[0])