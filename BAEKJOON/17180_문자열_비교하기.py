import sys
def input(): return sys.stdin.readline().strip()


_, str1, str2 = input(), input(), input()

if (len(str1) < len(str2)):
    str1, str2 = str2, str1
N, M = len(str1), len(str2)

dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]

for i in range(1, M):
    dp[i][0] = float('inf')
dp[0][0] = 0

for i in range(1, M + 1):
    for j in range(1, N + 1):
        dp[i][j] = abs(ord(str2[i - 1]) - ord(str1[j - 1]))

for j in range(1, N + 1):
    for i in range(1, M + 1):
        dp[i][j] = dp[i][j] + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

print(dp[M][N])
