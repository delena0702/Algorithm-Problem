import sys
def input(): return sys.stdin.readline().strip()


dp = [0, 1, 1, 1, 2, 2] + [0] * (95)
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

T = int(input())
for _ in range(T):
    print(dp[int(input())])
