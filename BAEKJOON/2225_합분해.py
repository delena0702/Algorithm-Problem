def combine(n, k):
    dp = [[1] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    return dp[n][k]

N, K = map(int, input().split())
MOD = 1000000000
print(combine(N, K - 1))