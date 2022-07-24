import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = list(map(int, input().split()))
dp, answer = [1] * N, 0
for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))