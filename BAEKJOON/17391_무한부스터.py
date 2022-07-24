import sys
INF = 987654321
def input(): return sys.stdin.readline().strip()

(N, M) = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [[INF]*M for _ in range(N)]
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if i == N-1 and j == M-1:
            dp[i][j] = 0
            continue
        for k in range(i+1, min(N, i+1+data[i][j])):
            dp[i][j] = min(dp[i][j], dp[k][j])
        for k in range(j+1, min(M, j+1+data[i][j])):
            dp[i][j] = min(dp[i][j], dp[i][k])
        dp[i][j] += 1
print(dp[0][0])