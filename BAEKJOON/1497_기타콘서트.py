import sys
def input(): return sys.stdin.readline().strip()

def dfs(idx, selected):
    if idx == N:
        if check.count(0) == M:
            return (-1, M + 1)
        return (M - check.count(0), -selected)
    
    retval = dfs(idx + 1, selected)

    for i in range(M):
        if arr[idx][1][i] == 'Y':
            check[i] += 1

    retval = max(retval, dfs(idx + 1, selected + 1))

    for i in range(M):
        if arr[idx][1][i] == 'Y':
            check[i] -= 1

    return retval

N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
check = [0] * M
answer = dfs(0, 0)
print(-1 if answer[0] == -1 else -answer[1])