import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))

dp = [0] * (N)
for i in range(N):
    dp[i] = data[i] + max(0, dp[i - 1])
print(max(dp))