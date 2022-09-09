N = int(input())
MOD = 1000000000

dp = [1] * 10
dp[0] = 0
for _ in range(N - 1):
    next_dp = [0] * 10
    for i in range(10):
        if i - 1 >= 0:
            next_dp[i] = (next_dp[i] + dp[i - 1]) % MOD
        if i + 1 < 10:
            next_dp[i] = (next_dp[i] + dp[i + 1]) % MOD
    dp = next_dp
print(sum(dp) % MOD)