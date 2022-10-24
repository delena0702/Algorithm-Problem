import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
brr = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        result[i][j] = arr[i][j] + brr[i][j]
for i in range(N):
    print(*result[i], sep=' ')