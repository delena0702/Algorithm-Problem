from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N, S, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True
for i in range(1, N + 1):
    for j in range(M + 1):
        for k in [j - arr[i - 1], j + arr[i - 1]]:
            if 0 <= k <= M and dp[i - 1][k]:
                dp[i][j] = True

for i in range(M, -1, -1):
    if dp[N][i]:
        print(i)
        break
else:
    print(-1)