import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    if i + 1 < N:
        dp[i] += 1
        h = arr[i + 1] - arr[i]
    for j in range(i + 2, N):
        if (arr[j] - arr[i]) / (j - i) > h:
            dp[i] += 1
            h = (arr[j] - arr[i]) / (j - i)

    if i - 1 >= 0:
        dp[i] += 1
        h = arr[i - 1] - arr[i]
    for j in range(i - 2, -1, -1):
        if (arr[j] - arr[i]) / (i - j) > h:
            dp[i] += 1
            h = (arr[j] - arr[i]) / (i - j)
print(max(dp))