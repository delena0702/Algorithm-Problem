import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
psum = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1]\
            - psum[i-1][j-1] + arr[i - 1][j - 1]

K = int(input())
for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    print(psum[r1][c1] + psum[r2][c2]\
        - psum[r1][c2] - psum[r2][c1])