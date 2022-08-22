N = int(input())
dp = (1, 1)
for i in range(N):
    dp = (dp[1] % 15746, (dp[0] + dp[1]) % 15746)
print(dp[0])
