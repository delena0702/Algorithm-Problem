import sys
def input(): return sys.stdin.readline().strip()

N, L, D = map(int, input().split())
d = D
while True:
    if d >= (L + 5) * N or d % (L + 5) >= L:
        print(d)
        break
    d += D