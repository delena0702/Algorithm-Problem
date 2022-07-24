import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    (c, r) = divmod(N - 1, H)
    print(r + 1, str(c + 1).zfill(2), sep='')