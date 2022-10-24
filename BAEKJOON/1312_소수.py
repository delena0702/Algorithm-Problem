import sys
def input(): return sys.stdin.readline().strip()

A, B, N = map(int, input().split())
A %= B
dp, cnt = [-1] * B, [-1] * B

for i in range(N):
    if i == N - 1:
        print((A * 10) // B)
        break
    A = (A * 10) % B