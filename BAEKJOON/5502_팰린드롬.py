import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = input()
dp = [[0] * (N) for _ in range(N)]

for e in range(N):
    for s in range(e, -1, -1):
        if s == e:
            dp[s][e] = 1
            continue
        if data[s] == data[e]:
            dp[s][e] = dp[s+1][e-1] + 2
        dp[s][e] = max(dp[s][e], dp[s+1][e], dp[s][e-1])
print(N - dp[0][N-1])
