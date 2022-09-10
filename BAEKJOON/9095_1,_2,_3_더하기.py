import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1] * (N + 1)
    if N >= 2:
        dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = sum(dp[i - 3:i])
    print(dp[N])