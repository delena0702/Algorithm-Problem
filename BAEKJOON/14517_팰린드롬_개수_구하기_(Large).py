import sys
input = sys.stdin.readline().strip()
N = len(input)
dp = [[0]*(N) for i in range(N)]

for end in range(N):
    for start in range(end, -1, -1):
        if start == end:
            dp[start][end] = 1
        elif end - start == 1:
            dp[start][end] = 3 if input[start] == input[end] else 2
        else:
            dp[start][end] = dp[start][end-1] + \
                dp[start+1][end]-dp[start+1][end-1]
            if input[start] == input[end]:
                dp[start][end] += dp[start+1][end-1] + 1
        dp[start][end] %= 10007

print(dp[0][N-1])