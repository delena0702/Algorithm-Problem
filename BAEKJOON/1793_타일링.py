import sys
def input(): return sys.stdin.readline().strip()

dp = [1] * (250 + 1)
dp[2] = 3
for i in range(3, 250 + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

while True:
    try:
        N = int(input())
        print(dp[N])
    except:
        break