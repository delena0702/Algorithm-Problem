import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

cnt = 0
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if arr[i][j] == 1:
            for ii in range(i + 1):
                for jj in range(j + 1):
                    arr[ii][jj] = 1 - arr[ii][jj]
            cnt += 1
print(cnt)