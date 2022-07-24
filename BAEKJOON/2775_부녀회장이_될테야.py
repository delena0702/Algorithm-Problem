import sys
def input(): return sys.stdin.readline().strip()

dp = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(1, 15):
        if i:
            if j > 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][1] = 1
        else:
            dp[0][j] = j
            

T = int(input())
for _ in range(T):
    k, n = int(input()), int(input())
    print(dp[k][n])