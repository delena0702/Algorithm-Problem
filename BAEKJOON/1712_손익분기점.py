import sys
def input(): return sys.stdin.readline().strip()

A, B, C = map(int, input().split())
if B < C:
    print(A // (C - B) + 1)
else:
    print(-1)