import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
sub_sum = [[0] * (N + 1) for _ in range(N + 1)]
data = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        sub_sum[i][j] = sub_sum[i - 1][j] + sub_sum[i][j - 1] +\
            data[i][j] - sub_sum[i - 1][j - 1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(sub_sum[y2 - 1][x2 - 1] + sub_sum[y1 - 2][x1 - 2] -
          sub_sum[y1 - 2][x2 - 1] - sub_sum[y2 - 1][x1 - 2])