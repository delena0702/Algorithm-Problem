import sys
def input(): return sys.stdin.readline().strip()

L, A, B, C, D = [int(input()) for _ in range(5)]
print(L - max((A - 1) // C, (B - 1) // D) - 1)