from math import isinf
import sys
sys.setrecursionlimit(30000)
def input(): return sys.stdin.readline().strip()

darr = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def dfs(x, y):
    if arr[y][x] == 'H':
        return 0
    if dp[y][x] != -1:
        return dp[y][x]
    if visited[y][x]:
        return float('inf')

    visited[y][x] = True
    value = int(arr[y][x])
    retval = 1
    for dx, dy in darr:
        nx, ny = x + value * dx, y + value * dy

        if not 0 <= nx < M:
            continue
        if not 0 <= ny < N:
            continue

        retval = max(retval, dfs(nx, ny) + 1)

    dp[y][x] = retval
    visited[y][x] = False
    
    return retval

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
answer = dfs(0, 0)
print(-1 if isinf(answer) else answer)