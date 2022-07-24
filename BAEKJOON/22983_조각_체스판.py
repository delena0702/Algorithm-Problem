import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
data = [input() for _ in range(N)]
dp, answer = [[1] * (M) for _ in range(N)], N * M

for i in range(1, N):
    for j in range(1, M):
        if data[i][j] != data[i - 1][j - 1] or\
            data[i][j] == data[i][j - 1] or\
            data[i][j] == data[i - 1][j]:
            continue
        
        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        answer = answer + dp[i][j] - 1

print(answer)