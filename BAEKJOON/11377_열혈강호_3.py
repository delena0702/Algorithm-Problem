import sys
def input(): return sys.stdin.readline().strip()


(N, M, K) = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split()[1:])))


def dfs(here, visited):
    if visited[here]:
        return 0
    visited[here] = True
    for there in arr[here]:
        if match[there] == -1 or dfs(match[there], visited):
            match[there] = here
            return 1
    return 0


answer = 0
match = [-1] * (M + 1)
for i in range(N):
    visited = [False] * N
    answer += dfs(i, visited)
cnt = 0
for i in range(N):
    visited = [False] * N
    if dfs(i, visited):
        answer += 1
        cnt += 1
    if cnt >= K:
        break
print(answer)
