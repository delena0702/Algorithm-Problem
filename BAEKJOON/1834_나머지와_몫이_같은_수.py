import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
print(N * (N - 1) * (N + 1) // 2)