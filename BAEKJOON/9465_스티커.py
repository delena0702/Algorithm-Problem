import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    dp = [0, 0, 0]

    for i in range(N):
        next_dp = [0, 0, 0]
        next_dp[0] = max(dp)
        next_dp[1] = data[0][i] + max(dp[0], dp[2])
        next_dp[2] = data[1][i] + max(dp[0], dp[1])
        dp = next_dp
    print(max(dp))
