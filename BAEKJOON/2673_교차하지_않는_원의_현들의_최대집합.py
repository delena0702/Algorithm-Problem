import sys
import collections

def input(): return sys.stdin.readline().strip()
link = collections.defaultdict(lambda: -1)
SIZE = 100

N = int(input())
for i in range(N):
    (a, b) = map(int, input().split())
    if a > b:
        a, b = b, a
    link[a-1] = b-1

dp = [[0]*SIZE for _ in range(SIZE + 1)]

for b in range(0, SIZE):
    for a in range(b - 1, -1, -1):
        dp[a][b] = dp[a+1][b]
        if a < link[a] and link[a] <= b:
            dp[a][b] = max(dp[a][b], dp[a + 1][link[a] - 1] +
                           dp[link[a] + 1][b] + 1)
print(dp[0][SIZE - 1])
